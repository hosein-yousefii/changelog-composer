# Markdown to Html converter

This task is able to convert markdown files to html.

## Dependencies

Image:

- changelog-base-image 


## Workspaces

- input-file-dir: Location where the md files are there.

- output-file-dir: Location where the html files will be there.


## Parameters

- compatibleToHtml: This enables you to skip the task in the pipeline, and will copy all md files to the output-file-dir in order to be accesible for the next task. (REQUIRED, default: "")

- baseImageVersion: This is the latest stable version of the changelog image. (REQUIRED, default: "")


## Test

In order to test this task, you need to apply the sample file in tests directory named sample-md-file.yaml which will create an md file.

Then you need to apply the taskRun, run.yaml

```
kubectl -n NAMESPACE apply -f tests/sample-md-file.yaml

kubectl -n NAMESPACE apply -f tests/run.yaml
```

## Usage:

You only need to apply task:
```
kubectl -n NAMESPACE apply -f markdown-to-html-converter.yaml
```
 
Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
