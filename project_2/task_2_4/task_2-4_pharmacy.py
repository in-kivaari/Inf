capsules = int(input("Введите общее количество произведенных капсул: "))
capsules_in_package= int(input("Введите количество капсул в одной упаковке: "))

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{capsules//capsules_in_package}\nОстаток капсул:\t\t{capsules%capsules_in_package}")