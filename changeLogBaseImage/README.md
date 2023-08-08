# ChangeLog Base Image

Include all necessary python packages in order to run changelog-composer tools. 

This is related to changelog composer tekton pipeline.

## Usage

You need to build this image and store it somewhere to be able to be fetched with tekton.

```
docker build . -t changelog-base-image
```


See requirements.txt for library details.

Copyright 2023 Hosein Yousefi <yousefi.hosein.o@gmail.com>
