user_input = int(input('Guess a number: '))
magic_num = 5

def magic(guess, magic_num):
    while guess != magic_num:
        guess = int(input('Guess a number: '))
        print("No sorry, try again!")
    print("Yes, you win!")

magic(user_input, magic_num)