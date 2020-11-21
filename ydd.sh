#!/bin/bash
# ydd
# Downloads all videos of a channel/user/playlist or list of videos with date
# ydd "<link> <link> ..."

url=$@

download_video () {
  youtube-dl --embed-subs --embed-thumbnail --add-metadata \
    --merge-output-format mkv --ignore-errors --sub-lang en \
    --cookies ~/.config/youtube-dl/cookies.txt \
    --output "%(upload_date)s %(title)s (%(id)s).%(ext)s" "$1"
}

if [[ "$url" =~ ( |\') ]]; then
  arr=($url)
  for each in "${arr[@]}"; do
    download_video $each
  done
else
  download_video $url
fi
