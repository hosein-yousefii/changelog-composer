# Changelog Generator

This task is able to generate changelog from your repository based on commit messages.

We decided to use a standard form of messages, like: fix: [JIRA-1235] Message related to commit.

## Dependencies

Tasks:

- git-clone

Image:

- changelog-base-image

ConfigMap:

- changelog-gen-jinja-template-file (you should create default jinja2 template for changelog, two samples exists in run folder which changelog-template.yaml  is the default template)


## Workspaces

- output: Location where source is stored.

- ssh-creds: Location where credentials for bitbucket is stored.

- changelog-file-dir: Location where the output will be stored.

- changelog-gen-jinja-template-dir: Location where the template(configMap) will be there.


## Parameters

- repoUrl: git repo url as used by git clone command.(REQUIRED, default: "")

- template-file: Name of the jnja2 template. (Optional, default: "template.jinja")

- output-file: Name of the generated changelog file. (Optional, default: "changelog.md")

- convention-commit-sections: List of convention sections which you want to filter. (Optional, default: "fix,feat")

- baseImageVersion: This is the latest stable version of the changelog image. (REQUIRED, default: "")

## Test

Make sure git-clone and changelog-generator tasks are applied.
Make sure you applied ConfigMap from (run/general-changelog-template.yaml).

Make sure you changed related parameters in (tests/pipeline.yaml)

```
kubectl -n NAMESPACE create -f tests/pipeline.yaml
```

## Usage

You need to apply these:
```
kubeclt -n NAMEPSACE apply -f changelog-template.yaml

kubectl -n NAMESPACE apply -f changelog-generator.yaml 
```

## Notes
If you want to generate changelog from whole commit messages choose the general-changelog-template.yaml as default template and apply it.

The changelog-template.yaml only catch the latest commit message.

Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
