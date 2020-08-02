leet_dict = {
    'A' : '4',
    'E' : '3',
    'G' : '6',
    'I' : '1',
    'O' : '0',
    'S' : '5',
    'T' : '7'
}

## PROGRAM

# my_string = "I am a leet programmer"
# for i in my_string:
#         if i.upper() in leet_dict:
#         print(leet_dict[i.upper()], end='')
#     else:
#         print(i, end='')




##FUNCTION

def leet_speak(my_string):
    leet_string = ''
    for i in my_string:
        if i.upper() in leet_dict:
            leet_string += (leet_dict[i.upper()])
        else:
            leet_string += (i)
    return leet_string




my_string = "I am a leet programmer"
print(leet_speak(my_string))