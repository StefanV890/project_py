import random
import time

points = {}
time_ = {}


def initalize_players(user_number):
    """
        Function for registering players
        ------
        Parameters:
        user_number(int) the number of the users
        ------
        Returns
        -initial player names
        -the index of the player
        -crates the points and time_ dictionary
    """
    for i in range(user_number):
        tx = "user name " + str(i+1) + ": "
        play = input(tx)
        points[play] = 0
        time_[play] = 0
        return points, time_

def start_game(name):
    """
        Function for starting game
        ------
        Parameters:
        name(str) the name of the user WHICH IS CURRENTLY PLAYING
        ------
        Returns
        -number of guesses
        -name of te player which was playing last
        -number of attempts
        ------
        Notes
        -uncomment line 48 for debug
        """
    t1 = int(time.time())
    print("Start game for ",name)
    guesses = []
    secret_number =  random.randint(1,100)
    tries = 0
    print("chose a number between 1-100")
    #print (secret_number) #debug
    while True:
        tries +=1
        key_number =int(input("type a number "))
        guesses.append(key_number)
        if secret_number < key_number:
            print("type a smaller number next time")
        elif secret_number > key_number:
            print("type a bigger number next time")
        else:
            t2 = int(time.time())
            #print(t2-t1)
            print(f"Your guesses: {guesses}")
            print(f"Good work {name}. You got it right in {tries} attempts\n")
            points[name]=tries
            time_[name]=t2-t1
            break
user_number = int(input("how many users "))
initalize_players(user_number)

for player in points.keys():
    print("")
    start_game(player)

print("RESULTS")
for player in points.keys():
    print(f"{player} - {points[player]} attemps in {time_[player]} seconds")