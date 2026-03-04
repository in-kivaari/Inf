#!/bin/bash

for i in {1..10}; do
    touch "test$i.txt"
done

while [ $i -gt 0 ]; do
    rm "test$i.txt"
    let "i--"
done
