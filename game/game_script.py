from .players import initialize_players, time_, points, Player
from os import strerror
import random
import time



class BoundariesException(Exception):
    pass

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
    try:
        t1 = int(time.time())
        guesses = []
        secret_number =  random.randint(1,100)
        tries = 0
        print("chose a number between 1-100")
        print (secret_number) #debug
        while True:
            tries +=1
            key_number =int(input("type a number "))
            if key_number < 1 or key_number > 100:
                raise BoundariesException
            guesses.append(key_number)
            if secret_number < key_number:
                print("type a smaller number next time")
            elif secret_number > key_number:
                print("type a bigger number next time")
            else:
                t2 = int(time.time())
                #print(t2-t1)
                print(f"Your guesses: {guesses}")
                print(f"You got it right in {tries} attempts\n")
                with open("C:/Users/Stefan/PYTHON/project_py/results", "at") as f:
                    f.write(f"Good work {name}. You got it right in {tries} attempts\n")
                    f.write(f"Your guesses: {guesses}\n")
                break
    except BoundariesException:
        print("Error: the value is not within permitted range (1..100)")
        start_game(name)
    except ValueError:
        print("Type a valid number")
        start_game(name)
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))

