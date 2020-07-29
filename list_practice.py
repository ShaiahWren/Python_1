##SMALL

#1

# num_list = [5, 4, 6, 7, 8, 9]

# acc =0

# for i in num_list:
#     acc += i
# print(acc)

# 2

# num_list = [5, 4, 6, 7, 8, 9]
# print(max(num_list))

# # 3
# num_list = [5, 4, 6, 7, 8, 9]

# print(min(num_list))

# ## 4
# num_list = [5, -44, 6, 7, -8, 9, 22, 24]

# for i in num_list:
#     if i % 2 == 0:
#         print(i)
#     else:
#         pass

## 5
# num_list = [5, -44, 6, 7, -8, 9, 22, 24]
# for i in num_list:
#     if i >= 0:
#         print(i)


# ## 6 
# num_list = [5, -44, 6, 7, -8, 9, 22, 24]
# new_num_list = []

# factor = 2
# for i in num_list:
#     new_num_list.append(i * factor)
# print(new_num_list)

## 7

# my_string = "Shaiah Wren"

# print(my_string[::-1])


## MEDIUM 
## 1
# list_1 = [2, 4, 5]
# list_2 = [2, 3, 6]
# new_list = []

# for i in range(len(list_1)):
#     new_list.append(list_1[i] * list_2[i])

# print(f"{list_1} X {list_2} = {new_list}")

## 2 (attempt 1)

# one_list = [ [1,3], [2,4]]
# two_list = [ [5,2], [1,0]]
# new_list = [ [], []]

# for i in range(len(one_list)):
#     for j in range(len(one_list[i])):
#         new_list[i].append(one_list[i][j] + two_list[i][j])
# print(new_list)

## 2 (Attempt 2)

one_list = [ [1,3], [2,4]]
two_list = [ [5,2], [1,0]]
new_list = [ [], []]

for i in range(len(one_list)):
    for j in range(len(one_list[i])):
        new_list[i].append(one_list[i][j] + two_list[i][j])
print(new_list)