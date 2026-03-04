#!/bin/bash

read -p "Введите текущий год: " CURRENT_YEAR
read -p "Введите год своего рождения: " BIRTH_YEAR

echo "Текущий год: $CURRENT_YEAR"
echo "Ваш примерный возраст: $((CURRENT_YEAR - BIRTH_YEAR))"
