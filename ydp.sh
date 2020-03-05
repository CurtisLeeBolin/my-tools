#!/bin/bash
# ydp
# Downloads all videos of a playlist(s)
# ydp <link> <link> ...

youtube-dl --continue --embed-subs --embed-thumbnail --add-metadata \
  --merge-output-format mkv --ignore-errors --sub-lang en --write-sub \
  --age-limit 30 \
  --output "%(autonumber)s %(title)s (%(id)s).%(ext)s" "$@"
