##Try 1
# while True:
#     day = int(input('Day (0-6)? '))
#     if day == 0:
#         print("Sunday")
#     elif day == 1:
#         print("Monday")
#     elif day == 2:
#         print("Tuesday")
#     elif day == 3:
#         print("Wednesday")
#     elif day == 4:
#         print("Thursday")
#     elif day == 5:
#         print("Friday")
#     elif day == 6:
#         print("Saturday")
#     else:
#         print("Try again")


##try 2
# func_dict = {
#     "0" : "Sunday",
#     "1" : "Monday",
#     "2" : "Tuesday",
#     "3" : "Wednesday",
#     "4" : "Thursday",
#     "5" : "Friday",
#     "6" : "Saturday"
# }

# def day_func(): 
#     day = ""
#     while day.lower() != "exit":
#         day = (input("Enter day '0—6': "))
#         try:
#             day_int = int(day)
#             print(func_dict[f"{day_int}"])
#         except:
#             if day.lower() == 'exit':
#                 print("Goodbye!")
#             else:
#                 print("Please enter '0—6' or 'Exit'")

# day_func()



# 4

day_dict = {
    "0" : "Sunday",
    "1" : "Monday",
    "2" : "Tuesday",
    "3" : "Wednesday",
    "4" : "Thursday",
    "5" : "Friday",
    "6" : "Saturday",
}


def day_func():
    while True:
        day = int(input('Day (0-6)? '))
        try:
            print(day_dict[f"{day}"])
        except:
            print("Please enter number '0-6': ")

day_func()
