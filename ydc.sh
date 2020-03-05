#!/bin/bash
# ydc
# Downloads all videos of a channel
# ydc <channel>

youtube-dl --continue --embed-subs --embed-thumbnail --add-metadata \
  --merge-output-format mkv --ignore-errors --sub-lang en --write-sub \
  --age-limit 30 \
  --output "%(upload_date)s %(title)s (%(id)s).%(ext)s" \
  "http://www.youtube.com/channel/$1"
