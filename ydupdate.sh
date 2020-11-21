#!/bin/bash
# ydupdate.sh

if ! which git; then
  sudo pacman -Sy git
fi

if [[ -z ~/Projects ]]; then
  mkdir ~/Projects
fi

cd ~/Projects

if [[ -z youtube-dl ]]; then
  git clone https://github.com/ytdl-org/youtube-dl.git
else
  cd youtube-dl
  git pull
fi
