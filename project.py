import random

def start_game():
    secret_number =  random.randint(1,100)
    tries = 0
    print("chose a number between 1-100")
    print (secret_number)
    while True:
        tries +=1
        key_number =int(input("type a number "))
        if secret_number < key_number:
            print("type a smaller number next time")
        elif secret_number > key_number:
            print("type a bigger number next time")
        else:
            print("good work you got it right :)")
            break
start_game()