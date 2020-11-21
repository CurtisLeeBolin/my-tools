#!/bin/bash

before="$1"
after="$3"

i=$2
for f in *; do
	if [ -f "$f" ]; then
		new=$(printf "%s%02d%s" "$before" "$i" "$after")
		mv -i -- "${f}" "${new}"
		let i=i+1
	fi
done
