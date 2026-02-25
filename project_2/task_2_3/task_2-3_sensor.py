operator_name = input("Введите имя оператора: ")
pressure_value= input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as sensor_log:
    sensor_log.write(f"Оператор\t{operator_name}\nДавления\t{pressure_value} Па")

print("Данные успешно сохранены в sensor_log.txt")
