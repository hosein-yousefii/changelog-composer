# Generate Confluence compatible pages

This task generate comptable files' to confluence page based on different parameters.

### YOU SHOULD READ THIS PART CAREFULLY

You are able to have "single page" or "main page with child page", Let's describe "main page with child page" first.

## Generate Page with child

Remember: You can't use this feature for multiple files at the same time.(exp: If you have multiple file in input-file-dir workspace, It doesn't work and it doesn't make sense.)

With this feature, two files will be created: something-main.html, something-child.html from the existing file under input-file-dir workspace.

In the main html file you can have "Header" and "Footer" parts, and the child page contains only the main information(content of file under input-file-dir workspace).

So you need to set these parameters:

compatibleToHtml: true

createChildPage: true

headerFooterTemplateName: Optional

headerString: Optional

footerString: Optional


Also if you want to use header and footer feature you can create a file in your repository with any name and set headerFooterTemplateName, if you want to have a general header footer template You can also implement it as configmap (exp: ./tests/sample-headerFooter-file.yaml).

If this file exists on both path the repository file will be taken.

Only main page contains header and footer not child page.


## Generate Single page

Remember: You are able to give multiple files and it will generate new files based on their names.

If you want to have "Header" and "Footer", and if you have multiple files then all new files will containe same header and footer, unless you disable this option by not to specifying the path.

So if you have one file then it's good to have header and footer parts.

You need to set these parameters:

compatibleToHtml: true

createChildPage: false

headerFooterTemplateName: Optional

headerString: Optional

footerString: Optional


## Dependencies

Image:

- changelog-base-image

## Wrokspaces

- output: Location where source is stored.(which can be an empty directory)

- input-file-dir: Where input files exists.

- output-file-dir: Where to store confluence pages.

- headerFooterTemplate-dir: Where to store header and footer template file. (Optional)


## Parameters

- baseImageVersion: Version of base changelog image.(REQUIRED, default: "")

- compatibleToHtml: Make pages compatible to Confluence Html format. (OPTIONAL, default "true") "Now we only support html"

- createChildPage: It will create child page. (OPTIONAL, default: "true")

- headerFooterTemplateName: This include header and footer for the page. (OPTIONAL, default: "ReleaseNotesTemplate.md")

- headerString: header string in template file.(OPTIONAL, default: "[header]")

- footerString: footer string in template file.(OPTIONAL, default: "[footer]")


## Test

To make a test you have all material you want undet tests folder.

```
kubectl apply -n NAMESPACE -f tests/sample-headerFooter-file.yaml

kubectl apply -n NAMESPACE -f tests/sample-html-file.yaml

kubectl apply -n NAMESPACE -f tests/run.yaml

```

Make sure parameters in run.yaml are correct.

## Usage

You need to install:

```
# If you have your own, install it instead of this one.
kubeclt apply -n NAMESPACE -f headerfooter-template-file.yaml

kubeclt apply -n NAMESPACE -f generate-confluence-compatible-pages.yaml
```


Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
