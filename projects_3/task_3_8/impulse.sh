#!/bin/bash

read -p "Введите имя гена: " name
read -p "Введите уровень экспрессии (целое число): " level

if [[ "$name" == "" || "$level" == "" ]]; then
    echo -e "\nНедостаточно данных!"
else
    echo -e "\nЭкспрессия гена $name составляет $level единиц"
fi
