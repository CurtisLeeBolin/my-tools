#!/bin/bash

file=${1}

ffmpeg -i "${file}" 2>&1 | grep --color=always "Stream #0:.*:\|Duration:*"
