## Try 1

# def day_func(): 
#     day = ""
#     while True:
#         day = (input("Enter day '0—6': "))
#         try:
#             day_int = int(day)
#             if day_int == 5 or day_int == 6:
#                 print("Sleep in!")
#             else:
#                 print("Go to work!")
#         except:
#             if day.lower() == 'exit':
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Please enter '0—6' or 'Exit'")

# day_func()


# Try 2

day_dict = {
    "0" : "Go to work!",
    "1" : "Go to work!",
    "2" : "Go to work!",
    "3" : "Go to work!",
    "4" : "Go to work!",
    "5" : "Sleep in!",
    "6" : "Sleep in!",
}


def day_func():
    while True:
        day = input('Day (0-6)? ')
        try:
            print(day_dict[f"{day}"])
        except:
            print("Please enter number '0-6': ")

day_func()