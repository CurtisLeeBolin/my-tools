#!/bin/bash
# yd
# Simplifies the use of youtube-dl (works with all site not just youtube)
# yd "<link> <link> ..."

url=$@

download_video () {
  youtube-dl --embed-subs --add-metadata \
    --merge-output-format mkv --ignore-errors --sub-lang en \
    --cookies ~/.config/youtube-dl/cookies.txt \
    --output "%(uploader)s - %(title)s (%(id)s).%(ext)s" "$1"
}

if [[ "$url" =~ ( |\') ]]; then
  arr=($url)
  for each in "${arr[@]}"; do
    download_video $each
  done
else
  download_video $url
fi
