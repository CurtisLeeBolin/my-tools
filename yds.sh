#!/bin/bash
# yds
# Downloads from a youtube search
# yds <number> <search terms>
#
# examples to download 10 Harlem Shake Videos:
#
# yds 10 Harlem\ Shake
# or
# yds 10 "Harlem Shake"

count="$1"
shift
youtube-dl --continue --embed-subs --embed-thumbnail --add-metadata \
  --merge-output-format mkv --ignore-errors --sub-lang en --write-sub \
  --age-limit 30 \
  --output "%(title)s (%(id)s).%(ext)s" \
  "ytsearch$count:$@"
