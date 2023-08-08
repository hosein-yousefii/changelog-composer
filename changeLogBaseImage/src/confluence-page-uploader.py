import requests
import sys

def upload_to_confluence(force_update_page, force_update_childpage, page_file, confluence_apikey, confluence_pagetitle, confluence_url, confluence_space,
                         childpage, confluence_childpage_title):
    childpage_id = "NONE"
    upload_update = 0
    upload_create = 0
    # Server availability
    url = confluence_url + "/rest/api"
    try:
        requests.head(url)
    except:
        print(f"[ERROR]: Confluence is not reachable, check if the url is correct: {url}")
        return 1

    # Authorization check
    headers = {"Authorization": f"Bearer {confluence_apikey}"}
    url = confluence_url + "/rest/api/space?limit=1&status=archived"
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if not data["results"]:
            print(f"[ERROR]: You're not authorised, make sure the confluence api key is correct.")
            return 1
    except requests.RequestException as e:
        print(f"[ERROR]: An error occurred: {e}")

    # Read page content
    with open(page_file, 'r') as file:
        page_content = file.read()

    if not page_content:
        print(f"[ERROR]: File {page_file} is empty.")
        return

    # Check if page exist to decide create new one or update it.
    url = confluence_url + "/rest/api/content"
    params = {"title": confluence_pagetitle, "spaceKey": confluence_space, "expand": "history"}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        headers = {"Authorization": f"Bearer {confluence_apikey}", "Content-Type": "application/json"}
    except:
        print(
          f"[ERROR]: Cannot get information about this page: {confluence_pagetitle}, you can make sure if the "
          f"inputs are correct: space={confluence_space}, params={params}")
        return

    if (data["results"] != []) and (childpage == "true"):
        childpage_url = data["results"][0]["_expandable"]["children"]

        # Get the child pages data
        try:
            page_url = confluence_url + childpage_url + "/page"
            response = requests.get(page_url, headers=headers)
            childpage_data = response.json()
        except:
            print(f"[ERROR]: couldn't fetch childpage data from: {url}")
            return

        if not confluence_childpage_title:
            # Extract childpage Title which is the latest version.
            start_index = page_content.find("<a href=''>")
            end_index = page_content.find("</a>", start_index)

            if start_index != -1 and end_index != -1:
                childpage_title = page_content[start_index + len("<a href=''>"):end_index]
            else:
                print("[ERROR]: Couldn't find Version number.")
                return
        else:
            childpage_title = confluence_childpage_title

        # Find if there is a child page with the same name.
        if childpage_data["results"]:
            matching_ids = [item["id"] for item in childpage_data["results"] if item["title"] == childpage_title]

            if matching_ids:
                childpage_id = matching_ids[0]

    # Create new page or child page if it doesn't exist.
    if (childpage == "true") and (data["results"] == []):
        print(f"[ERROR]: Main page ({confluence_pagetitle}) in this space ({confluence_space}) doesn't exist.")
        return

    # create new child page
    elif (childpage == "true") and (data["results"] != []) and (childpage_id == "NONE"):
        page_id = data["results"][0]["id"]
        data = {
            "type": "page",
            "title": childpage_title,
            "ancestors": [
                {
                    "id": page_id
                }
            ],
            "space": {
                "key": confluence_space
            },
            "body": {
                "storage": {
                    "value": page_content,
                    "representation": "storage"
                }
            }
        }
        upload_create = 1
        page_title = childpage_title

    # create new page
    elif (childpage == "false") and (data["results"] == []):
        data = {
            "type": "page",
            "title": confluence_pagetitle,
            "space": {
                "key": confluence_space
            },
            "body": {
                "storage": {
                    "value": page_content,
                    "representation": "storage"
                }
            }
        }
        upload_create = 1
        page_title = confluence_pagetitle

    # Update main page
    elif (childpage == "false") and (data["results"] != []):
        if force_update_page.lower() == "true":
            page_id = data["results"][0]["id"]
            page_url = confluence_url + f"/rest/api/content/{page_id}"
            # gather the current version of the page
            try:
                response = requests.get(page_url, headers=headers)
            except:
                print(f"[ERROR]: Couldn't fetch page ({confluence_pagetitle}) version.")
                return
            data = response.json()
            version = data["version"]["number"] + 1
            # Update the page with new data
            data = {
                "id": page_id,
                "type": "page",
                "title": confluence_pagetitle,
                "space": {
                    "key": confluence_space
                },
                "body": {
                    "storage": {
                        "value": page_content,
                        "representation": "storage"
                    }
                },
                "version": {
                    "number": version
                }
            }
            upload_update = 1
            url = url + f"/{page_id}"
            page_title = confluence_pagetitle
        else:
            upload_update = 0
            print(f"[ERROR]: Can not update existing page unless it is forced by setting force_update_page=true.")
            return

    # update child page
    elif (childpage == "true") and (data["results"] != []) and (childpage_id != "NONE"):
        if force_update_childpage.lower() == "true":
            page_id = data["results"][0]["id"]
            page_url = confluence_url + f"/rest/api/content/{childpage_id}"
            # gather the current version of the page
            try:
                response = requests.get(page_url, headers=headers)
            except:
                print(f"[ERROR]: Couldn't fetch page ({confluence_pagetitle}) version.")
                return
            data = response.json()
            version = data["version"]["number"] + 1
            # Update the page with new data
            data = {
                "id": childpage_id,
                "type": "page",
                "title": childpage_title,
                "ancestors": [
                    {
                        "id": page_id
                    }
                ],
                "space": {
                    "key": confluence_space
                },
                "body": {
                    "storage": {
                        "value": page_content,
                        "representation": "storage"
                    }
                },
                "version": {
                    "number": version
                }
            }
            upload_update = 1
            url = url + f"/{childpage_id}"
            page_title = childpage_title
        else:
            upload_update = 0
            print(f"[ERROR]: Can not update existing childpage unless it is forced by setting force_update_childpage=true.")
            return

    # Upload page
    if upload_update == 1:
        try:
            requests.put(url, headers=headers, json=data)
        except:
            print(f"[ERROR]: Couldn't update the {page_title}")
            return

        page_link = confluence_url + f"/display/{confluence_space}/{page_title}"
        print(f"[INFO]: Page {page_title} updated successfully.")
        print(f"[INFO]: Find this page here: {page_link}")

    if upload_create == 1:
        try:
            requests.post(url, headers=headers, json=data)
        except:
            print(f"[ERROR]: Couldn't create the {page_title}")
            return

        page_link = confluence_url + f"/display/{confluence_space}/{page_title}"
        print(f"[INFO]: Page {page_title} created successfully.")
        print(f"[INFO]: Find this page here: {page_link}")


force_update_page = sys.argv[1]
force_update_childpage = sys.argv[2]
input_file = sys.argv[3]
apikey = sys.argv[4]
pagetitle = sys.argv[5]
host_url = sys.argv[6]
space = sys.argv[7]
child_page = sys.argv[8]
try:
    childpagetitle = sys.argv[9]
except:
    childpagetitle = ""

upload_to_confluence(force_update_page, force_update_childpage, input_file, apikey, pagetitle, host_url, space, child_page, childpagetitle)

