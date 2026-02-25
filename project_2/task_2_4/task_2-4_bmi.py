weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (см): "))

bmi = weight / ((height/100) ** 2)
print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height:.2f} см\nВес:\t{weight:.2f} кг\nИндекс массы тела пациента: {bmi:.2f}")