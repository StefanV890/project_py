import random

def start_game():
    guesses = []
    secret_number =  random.randint(1,100)
    tries = 0
    print("chose a number between 1-100")
   # print (secret_number) ###debug
    while True:
        tries +=1
        key_number =int(input("type a number "))
        guesses.append(key_number)
        if secret_number < key_number:
            print("type a smaller number next time")
        elif secret_number > key_number:
            print("type a bigger number next time")
        else:
            print("your guesses are ", guesses )
            print("good work you got it right :)")
            break
start_game()