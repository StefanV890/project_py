from .players import initialize_players, time_, points
import random
import time

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