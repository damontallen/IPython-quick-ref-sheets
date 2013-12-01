#!/bin/sh
kill $(ps ax | grep "ipython" | awk ' { print $1 } ')
kill $(ps ax | grep "Ipython" | awk ' { print $1 } ')
