#!/bin/bash

df -h | awk 'NR>1 {
    use = $5
    gsub(/[^0-9]/, "", use)
    if ((use+0) >= 90)
        print "Осторожно, Файловая система " $1 " загружена больше, чем на 90%"
}'
df -h | awk 'NR>1 { print $1 "\t" $5 }'
