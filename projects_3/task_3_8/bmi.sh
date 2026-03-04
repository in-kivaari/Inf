#!/bin/bash

read -p "Введите ваш вес (в кг): " weigh
read -p "Введите ваш рост(в сантиметрах): " high

bmi=$(((weigh*10000)/(high * high)))

echo "Ваш индекс массы тела составляет: $bmi"
