import os
import sys

releaseNotesTemplate_filePath = sys.argv[1]
start_string = sys.argv[2]
end_string = sys.argv[3]
main_content = sys.argv[4]
mainPage = sys.argv[5]
output = sys.argv[6]

def extract_between_strings(releaseNotesTemplate_filePath, start_string, end_string):
  with open(releaseNotesTemplate_filePath, 'r') as file:
    content = file.read()

  start_index = content.lower().find(start_string)
  end_index = content.lower().find(end_string)

  if end_string == "end_of_file":
    end_index = None

  if (start_index == -1 or end_index == -1) and len(content) != 0:
    print(f"[ERROR]: File should contain {start_string} and {end_string} tag Header or Footer string not found in the file.")

  start_index += len(start_string)
  extracted_content = content[start_index:end_index].strip()

  return extracted_content


def create_page(mainPage, main_content, header_content, footer_content, output_filePath):
  htmlOpenTag = "<h4>"
  htmlCloseTag = "</h4>"

  if mainPage.lower() == "true":
    confluenceCompatible_Header = ""
    main_content = "<p><ac:structured-macro ac:name='children' ac:schema-version='2' ac:macro-id='0ec2fb0e-eca1-4f00-b4cc-94dbc89b7b7b'><ac:parameter ac:name='all'>true</ac:parameter><ac:parameter ac:name='style'>h2</ac:parameter><ac:parameter ac:name='sort'>creation</ac:parameter><ac:parameter ac:name='reverse'>true</ac:parameter><ac:parameter ac:name='excerptType'>rich content</ac:parameter></ac:structured-macro></p>"
    confluenceCompatible_Footer = ""
  else:

    confluenceCompatible_Header = "<ac:structured-macro ac:name='html' ac:schema-version='1' ac:macro-id='cf730d54-5751-4cec-9461-28c790b9fc37'><ac:plain-text-body><![CDATA["
    confluenceCompatible_Footer = "]]></ac:plain-text-body></ac:structured-macro>"

  content_with_header_footer = htmlOpenTag + header_content.replace("\n","</h4>\n<h4>") + htmlCloseTag
  content_with_header_footer += main_content
  content_with_header_footer += htmlOpenTag + footer_content.replace("\n","</h4>\n<h4>") + htmlCloseTag
  confluenceCompatible = confluenceCompatible_Header + content_with_header_footer.replace("\"","'") + confluenceCompatible_Footer

  with open(output_filePath, "w") as file:
    file.write(confluenceCompatible)  

  print(f"[INFO]: Page created successfully!, find it here {output_filePath}")
  return confluenceCompatible

header_content = extract_between_strings(releaseNotesTemplate_filePath, start_string, end_string)
footer_content = extract_between_strings(releaseNotesTemplate_filePath, end_string, "end_of_file")
page = create_page(mainPage, main_content, header_content, footer_content, output)

print(page)
