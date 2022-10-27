#!/bin/sh

devpath="/dev/sda1"
maxwait=10

for (( i = 0; i <= $maxwait; i++ ))
do
  [ -b $devpath ] && exit 0
  echo -n "."
  sleep 1
done
exit 1
