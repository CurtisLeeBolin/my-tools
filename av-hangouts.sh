#!/bin/bash

IN_DIR="0in"
OUT_DIR="0out"

mkdir "${IN_DIR}" "${OUT_DIR}"

for each in "$@"; do

  fileName="${each}"

  mv "${fileName}" "${IN_DIR}"/"${fileName}"

	#ffmpeg -ss 00:00:02 -t 00:00:05 -i "${IN_DIR}"/"${fileName}" -filter:v "drawbox=x=1146:y=637:w=118:h=68:color=black@1:t=max" -c:v libx265 -c:a copy "${OUT_DIR}"/"${fileName}"
	ffmpeg -ss 00:00:02 -i "${IN_DIR}"/"${fileName}" -filter:v "drawbox=x=1146:y=637:w=118:h=68:color=black@1:t=max" -c:v libx265 -c:a copy "${OUT_DIR}"/"${fileName}"

done
