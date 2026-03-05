#!/bin/bash

read -p "Введите ваш вес (в кг): " weight
read -p "Введите ваш рост(в сантиметрах): " high

bmi=$(((weight*10000)/(high * high)))

echo "Ваш индекс массы тела составляет: $bmi"
