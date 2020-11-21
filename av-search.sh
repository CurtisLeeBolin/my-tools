#!/bin/bash

query="$@"

find /{home,srv}/lee/{Videos,.tmp/{saved,snark,process,done}}/ -iname "${query}*" 2>/dev/null
