# changelog-composer

[![GitHub license](https://img.shields.io/github/license/hosein-yousefii/changelog-composer)](https://github.com/hosein-yousefii/changelog-composer/blob/master/LICENSE)
![LinkedIn](https://shields.io/badge/style-hoseinyousefi-black?logo=linkedin&label=LinkedIn&link=https://www.linkedin.com/in/hoseinyousefi)

This is a Tekton pipeline which help you to auto generate changelog.

The purpose is to commit a message with tag like this:
```
git commit -am "feat: [SAM-3363] Add force update"
git tag -a "v0.6.5" -m "feature"

```

Then push to repository then after Tekton changelog-composer pipeline triggered, You see something like this in Confluence:

<img width="900" src="https://github.com/hosein-yousefii/changelog-composer/blob/main/changelog-composer.jpg">


## Usage

Shortly I want to describe how to use this pipeline.

1- You need to build the image which is named: changeLogBaseImage, then push it somewhere accessible by tekton.

2- each tasks has its own readme which explain them completely, based on those you are able to install tasks.

3- then you need to at this pipeline to your original pipeline.

## Features

- You are able to use each task seperately.
- have your own changelog template to be able to filter commit messages. (https://github.com/hosein-yousefii/changelog-composer/blob/main/changelog-generator/0.1/changelog-template.yaml)
- add extra conventional commit sections
- Convert multiple markdown file to html with markdown-to-html-converter task.
- create one confluence page or creae a page with childs. (configured via createChildPage parameter)
- Have your own header and footer template to be placed on the page.
- You can have your header footer template file either in your repository or generally in your namespace as configMap.
- Upload multiple single pages at the same time with confluence-page-uploader task.
- Upload main page and child page.
- You can force to update existing pages.

## Remember
I suggest execute each task with their samples and get familiar with the whole task.
Then go through the whole pipeline and play with different parameters.
Now, you are ready to customize your own pipeline.

## contribute
Do you want to contribute so, don't waste your time and send me an email: Yousefi.hosein.o@gmail.com

Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>



