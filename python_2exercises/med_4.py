list_1 = [2, 4, 5]
list_2 = [2, 3, 4]
new_list = []

for i in list_1:
    for j in list_2:
        new_list.append(i * j)
    print(new_list)
