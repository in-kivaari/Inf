env_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{env_name}\n\n1. Концентрация агара - {agar_concentration}%\n2. Температура стерилизации - {sterilization_temperature}°C")

print("Файл 'recipe.txt' успешно сформирован!")
