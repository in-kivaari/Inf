#!/bin/bash

file="./log.sh"
error=0

if [ -f "$file" ]; then
    echo "Файл отчета существует"
else
    echo "Ошибка: файл не существует."
fi

case $error in
    0)
        echo "Статус: Ошибок нет." ;;
    1)
        echo "Статус: Критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac
