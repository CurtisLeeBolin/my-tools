#!/bin/bash
# Use this to split by chapter.
# Once you know last chapter of each
# episode, run the following:
# $ mkvmerge -o fileOut.mkv --split chapters:1,2,3 0in/fileIn.mkv

IN_DIR="0in"
OUT_DIR="0out"

mkdir "${IN_DIR}" "${OUT_DIR}"

for i in *.mkv; do
  mv "${i}" "${IN_DIR}"/"${i}"
  mkvmerge -o "${OUT_DIR}"/"${i}" --split chapters:all "${IN_DIR}"/"${i}"
done
