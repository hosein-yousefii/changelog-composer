# Changelog composer

This pipeline generate changelog from application repository based on conventional commit messages.

There are 4 main part (Tasks):

- changelog-generator: responsible to generate changelog based on a provided templpate and save it as a file.

- markdown-to-html-converter: This task convert the markdown files to html one.

- generate-confluence-compatible-page: in charge of Generating Page and child page and make it compatible to confluence.

- confluence-page-uploader: Uploads single page and childpage to confluence space.


Recommended to first check those tasks then use this pipeline.

## Dependencies

Image: changelog-base-image 

## Workspaces

- "source-ws": "Location where source is cloned/checked out to"
- "ssh-creds": "git ssh credentials - see https://hub.tekton.dev/tekton/task/git-clone"
- "changelog-file-ws": "Generated changelog will store here"
- "changelog-gen-jinja-template-ws": "Where changelog generator template is stored"
- "converted-file-ws": "where markdown/html files are stored.(based on convertToHtml descision)"
- "confluence-page-ws": "Where compatible confluence pages will be stored."
- "headerFooterTemplate-ws": "Where the default Header Footer template for the namespace is stored."

## parameters

Git
- name: "repoUrl"
  description: "ssh url of your repository"
- name: "REPO_NAME"
  description: "The name which will be used as part of page title."

changelog generator
- name: "baseImageVersion"
  description: "base image version."

markdown to html converter
- name: "compatibleToHtml"
  description: "Make decision based on this to convert files to html format."

generate confluence compatible page
- name: "createChildPage"
  description: "Create child page and main page."

upload confluence pages
- name: "apiKey"
  description: "Confluence api key."
- name: "pageTitle" 
  description: "Title of the page."
  default: "$(params.REPO_NAME)"
- name: "space"
  description: "Where in confluence page should be uploaded."
- name: "forceUpdatePage"
  description: "Force page to be updated if there is a same page."
  default: "true"
- name: "forceUpdateChildpage"
  description: "Force child page to be updated if there is a same child page."
  default: "false"

## Test

Make sure all tasks with their dependencies are applied then apply the run in tests folder

```
kubectl apply -n NAMESPACE tests/run.yaml
```

Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
