def f(s): #эта функция дает на выходе массив со строчками длинной меньше 45.
    k="" #вспомогательная строка для набора слов в массив list
    c=0 # счетчик для набора в массив list
    list=[]  #Массив со словами
    s_new="" #вспомогательная строка для набора слов в массив list1
    list1=[] #Массив со строчками длинной меньше 45.

    while c<len(s):
        if s[c]!=" ":
            k+=s[c]
            c+=1
        else:
            list.append(k)
            k=""
            c+=1
    list.append(k)

    for i in list:
        if len(s_new) + len(i) <=44:
            s_new= s_new + i + " "
        else:
            list1.append(s_new)
            s_new = i + " "
    list1.append(s_new)
    return list1        

researcher_name = input("Введите ваше имя: ")
research_data = input("Введите дату: ")
research_name = input("Введите имя эксперимента: ")
research_result = input("Введите вывод эксперимента: ")



print("+", 45*"-", "+")
print("| Электронный лабораторный журнал\t\t|")
print("+", 45*"-", "+")
print(f"| ФИО исследователя : {researcher_name}\t|")
print("+", 45*"-", "+")
print(f"| Дата\t\t:\t{research_data}\t\t|")
print("+", 45*"-", "+")
print(f"| Эксперимент\t:\t{research_name}\t|")
print("+", 45*"-", "+")
print(f"| Вывод:\t\t\t\t\t|")
for i in f(research_result):      
        if len(i)<6:
                print(f"| {i}\t\t\t\t\t\t|")
        if 5<len(i)<14:
                print(f"| {i}\t\t\t\t\t|")
        if 13<len(i)<22:
                print(f"| {i}\t\t\t\t|")
        if 21<len(i)<30:
                print(f"| {i}\t\t\t|")
        if 29<len(i)<38:
                print(f"| {i}\t\t|")
        if 37<len(i)<45:
                print(f"| {i}\t|")
print("+", 45*"-", "+")