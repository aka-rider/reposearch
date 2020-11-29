#!/bin/bash

NEEDLE="cache"


curl "https://api.github.com/search/repositories?q=${NEEDLE}" > github.json
curl --header "PRIVATE-TOKEN: ${GITLAB_PRIVATE_TOKEN}" "https://gitlab.com/api/v4/search?scope=projects&search=${NEEDLE}" > gitlab.json