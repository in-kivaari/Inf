#!/bin/bash

check_root() {
    if [ $EUID != 0 ]; then
        echo "Ошибка доступа. Вы не можете выполнять этот скрипт."
        exit 1
    fi
}
check_root
