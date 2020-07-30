my_list = ["Julian", "Buttercup", "Shaiah", "Hannah", "Lior"]

# c = 0
# while c < len(my_list):
#     print(my_list[c])
#     c += 1


# my_fam = []
# my_fam.append("Julian")
# print(my_fam)


## APPEND
# my_fam.append("Buttercup")
# print(my_fam)

## REMOVE
my_list.remove("Buttercup")

for i in my_list:
    if i == "Shaiah":
        print(i)
        break

if "Julian" in my_list:
    print("LOVE IT")
else:
    print("Where is Julian??")