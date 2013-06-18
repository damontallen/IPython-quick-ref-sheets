#!/bin/sh
kill $(ps ax | grep "ipython3 notebook --pylab inline" | grep " python3 " | awk ' { print $1 } ')
