# Confluence page uploader

This task upload confluence pages. There are two modes:

single page: which is just a page.

Child page: which is under a main page.

which both are supported.

### READ this part carefully

This task is able to upload more than one pages at the same time by set this parameter: createChildPage: false

Then it looks the mounted input directory (workspace) and upload each html file with the title of their file name.

If you want to have a child page the parameter createChildPage: true is necassary, also bulk upload is not supported.

___________________________________________________

Currently, we only support html files, so htmlFormat: true

## How to?

This task try to find if the page with same title exists then update it otherwise will create new page.

## Dependencies

- Image: changelog-base-image

## workspaces:

- input-file-dir: Where confluence pages exists

## parameters:

- baseImageVersion: Version of base changelog image.(REQUIRED, default: "")

- htmlFormat: pages are compatible to Confluence Html format. (OPTIONAL, default "true") "Now we only support html"

- childPgaeMode: child page mode uploads main page and one childpage. (OPTIONAL, default: "true")

- apiKey: Confluence api key. (REQUIRED, default: "")

- pageTitle: Title of the main page in childmode. (REQUIRED, default: "")

- serverUrl: Url of the server. (REQUIRED, default: "http://confluence.com")

- space: Confluence space where you want to upload. (REQUIRED, default: "")

- forceUpdatePage: Force page to be updated if there is a same page. (REQUIRED, default: "false")

- forceUpdateChildpage: Force child page to be updated if there is a same child page. (REQUIRED, default: "false")

## Test

In order to make a test, You have two sample in tests folder:

sample-html-main-child-page.yaml: which contain two files and createChildPage should be enabled

sample-html-main-pages.yaml: which three files exists and createChildPage should be disabled

```
k apply -f headerFooter-template-file.yaml

k apply -f tests/run.yaml

```

Remember: if you don't want to use child pages, after applying the sample you need to change the run.yaml parameters.

Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
