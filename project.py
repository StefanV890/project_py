

import random
import time

punctaj = {}
timp = {}


def start_game(name):
    t1 = int(time.time())
    print("Start game for ", name)
    guesses = []
    secret_number = random.randint(1, 100)
    tries = 0
    print("chose a number between 1-100")
    print(secret_number)  # debug
    while True:
        tries += 1
        key_number = int(input("type a number "))
        guesses.append(key_number)
        if secret_number < key_number:
            print("type a smaller number next time")
        elif secret_number > key_number:
            print("type a bigger number next time")
        else:
            t2 = int(time.time())
            # print(t2-t1)
            print(f"Your guesses: {guesses}")
            print(f"Good work {name}. You got it right in {tries} attempts\n")
            print("")
            punctaj[name] = tries
            timp[name] = t2 - t1
            break


user_number = int(input("how many users "))
for i in range(user_number):
    tx = "user name " + str(i + 1) + ": "
    play = input(tx)
    punctaj[play] = 0
    timp[play] = 0

for player in punctaj.keys():
    print("")
    start_game(player)

print("RESULTS")
for player in punctaj.keys():
    print(f"{player} - {punctaj[player]} attemps in {timp[player]} seconds")

