#!/bin/bash
# ydp
# Downloads all videos of a channel/user/playlist with numbering
# ydp "<link> <link> ..."

url=$@

download_video () {
  youtube-dl --embed-subs --embed-thumbnail --add-metadata \
    --merge-output-format mkv --ignore-errors --sub-lang en \
    --cookies ~/.config/youtube-dl/cookies.txt \
    --output "%(autonumber)s %(title)s (%(id)s).%(ext)s" "$1"
}

download_video $url
