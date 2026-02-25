reagent_name = input("Ведите названеи реагента: ")
reagent_quantity = int(input("Ведите количество: "))
reagent_input = f"Реактив [{reagent_name}] поступил на склад в количестве {reagent_quantity} шт."

print(reagent_input)

f = open(r"C:\Users\abaka\Desktop\abakanova_le\project_2\task_2_2\inventory.txt", "w", encoding="utf-8")
print(reagent_input, file=f)
f.close()