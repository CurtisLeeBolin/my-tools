#!/usr/bin/env bash

length=$1

if [ "$2" == "w" ]; then
	echo "${length} write"
else
	echo "${length} echo"
fi
