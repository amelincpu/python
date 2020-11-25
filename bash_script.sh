#!/bin/bash
echo "Hello World!"
while [ true ] ; do
read -n 1
if [ $? = 0 ] ; then
exit ;
fi
done