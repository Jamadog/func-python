
import random

def random_stringCreate(length):
    letters_ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters_eng = 'abcdefghijklmnopqrstuvwxyz'
    letters_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters_RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    letters_Num = '1234567890'

    print("----- choose an example of letters -----")
    print('1 -> '+ letters_ENG)
    print('2 -> '+ letters_eng)
    print('3 -> '+ letters_rus)
    print('4 -> '+ letters_RUS)
    choice_letters = int(input())

    print("with numbers?")
    print('1 -> Yes')
    print('2 -> No')
    print("enter 1 or 2")
    choice_num = int(input())

    if (choice_letters == 1):
        letters = letters_ENG
    elif (choice_letters == 2):  
        letters = letters_eng
    elif (choice_letters == 3):  
        letters = letters_rus
    elif (choice_letters == 4):  
        letters = letters_RUS
    
    if (choice_num == 1):
        letters += letters_Num
    print('how much do you need?')
    x = int(input())

    print('\n'.join((''.join(random.choice(letters) for i in range(length))) for x in range(x)))
    #for i in range(n):
    #    rand_string = ''.join(random.choice(letters) for i in range(length))
    #    print("Your string is: ")
    #    print(rand_string)


print("enter you number of elements ->")
n = int(input())
random_stringCreate(n)