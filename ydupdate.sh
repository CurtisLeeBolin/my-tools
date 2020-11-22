#!/bin/bash
# ydupdate.sh

if ! which git; then
  sudo pacman -Sy git
fi

if ! [ -d ~/Projects ]; then
  mkdir ~/Projects
fi

cd ~/Projects

if [ -d youtube-dl ]; then
  cd youtube-dl
  git pull
else
  git clone https://github.com/ytdl-org/youtube-dl.git
fi
