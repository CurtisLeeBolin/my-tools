#!/bin/bash
# dl
# Simplifies the use of curl
# dl "<link> <link> ..."

USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36)"

#USER_AGENT="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"

curl --user-agent "$USER_AGENT" --location --remote-name-all $@
