#!/bin/bash
# ydd
# Downloads all videos of a channel/user/playlist or list of videos with date
# ydd "<link> <link> ..."

url=$@

download_video () {
	while true; do
 		youtube-dl --embed-subs --add-metadata \
    	--merge-output-format mkv --ignore-errors --sub-lang en \
    	--cookies ~/.config/youtube-dl/cookies.txt \
    	--output "%(upload_date)s %(uploader)s - %(title)s (%(id)s).%(ext)s" "$1"
		if [[ $? -eq 0 ]]; then
      break
    fi
	done
}

if [[ "$url" =~ ( |\') ]]; then
  arr=($url)
  for each in "${arr[@]}"; do
    download_video $each
  done
else
  download_video $url
fi
