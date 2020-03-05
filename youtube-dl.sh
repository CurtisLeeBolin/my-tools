#!/bin/bash

PYTHONPATH=${HOME}/Projects/youtube-dl/:${PYTHONPATH} python \
  ${HOME}/Projects/youtube-dl/youtube_dl "$@"
