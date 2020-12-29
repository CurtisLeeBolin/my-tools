#!/bin/bash
# yds
# Downloads from a youtube search
# yds <number> <search term>
#
# examples to download 10 Harlem Shake Videos:
#
# yds 10 Harlem\ Shake
# or
# yds 10 "Harlem Shake"


count="$1"
shift
search_term=$@

download_video () {
  youtube-dl --embed-subs --embed-thumbnail --add-metadata \
    --merge-output-format mkv --ignore-errors --sub-lang en \
    --cookies ~/.config/youtube-dl/cookies.txt \
    --output "%(uploader_id)s - %(title)s (%(id)s).%(ext)s" "ytsearch$count:$search_term"
}

download_video $search_term
