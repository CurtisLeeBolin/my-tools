#!/bin/bash

for i in ~/Projects/my-tools/*.{py,sh}; do
	j="${i##*/}"
  j="${j%.??}"

	if [ -f ~/.local/bin/"${j}" ]; then
 		rm ~/.local/bin/"${j}"
	fi

  ln -s "${i}" ~/.local/bin/"${j}"
done
