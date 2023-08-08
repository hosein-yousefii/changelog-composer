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


