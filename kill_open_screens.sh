#!/bin/bash
par="$1"
session_name="${par:="ProgramGenerator"}"
#echo $session_name


# Get the process IDs of all screen sessions with the name "foo"
pids=$(screen -ls | grep -w $session_name | awk '{print $1}' | cut -d . -f1)
# Kill each process
for pid in $pids; do
  kill $pid
done