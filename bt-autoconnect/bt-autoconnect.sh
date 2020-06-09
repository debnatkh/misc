#!/usr/bin/env bash

RETRY=10
list_file="$HOME/.config/bt-autoconnect.list"
grep_line=\($(cat $list_file | awk '/START/{if (x)print x;x="";next}{x=(!x)?$0:x"|"$0;}END{print x;}' )\)

SAVEIFS=$IFS
IFS=$'\n'
devices=($(bt-device -l | grep -P $grep_line | grep -ohP "\(.*\)" | awk '{print substr($0, 2, length($0) - 2)}'
))
IFS=$SAVEIFS

for ((n=0;n<$RETRY;n++))
do 
	for var in "${devices[@]}"
	do
		echo $var
	  	bluetoothctl connect ${var}
		if [ $? -eq 0 ]; then
			echo OK
			exit 0
	  	else
	    	echo FAIL
	    	sleep 0.1
		fi
	done
done
exit 1

