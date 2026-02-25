protein_volum = int(input("Введите массу белков в продукте (г): "))
fat_volum = int(input("Введите массу жиров в продукте (г): "))
carb_volum = int(input("Введите массу углеводов в продукте (г): "))

print(f"Общая каллорийность продукта: {protein_volum * 4 + fat_volum  *9 + carb_volum * 4}")