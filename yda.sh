#!/bin/bash
# yda
# Simplifies the use of youtube-dl to download audio from youtube
# yda "<link> <link> ..."

url=$@

download_video () {
	youtube-dl --continue --format=bestaudio --ignore-errors \
		--age-limit 30 \
		--output "%(title)s (%(id)s).ogg" "$1"
}

if [[ "$url" =~ ( |\') ]]; then
  arr=($url)
  for each in "${arr[@]}"; do
    download_video $each
  done
else
  download_video $url
fi
