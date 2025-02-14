import random
import time


points = {}
time_ = {}

def start_games(name, guesses):
    """
    Function for starting game
    ------
    Parameters:
    name(str): the name of the user WHICH IS CURRENTLY PLAYING
    guesses(list): a list of guesses made by the player
    ------
    Returns:
    - number of guesses
    - name of the player which was playing last
    - number of attempts
    ------
    Notes:
    - This function assumes that guesses are provided in a list.
    """
    try:
        t1 = int(time.time())
        print("Start game for ", name)
        secret_number = random.randint(1, 100)
        tries = 0
        print("Chose a number between 1-100")
        # print(secret_number) #debug

        for key_number in guesses:
            tries += 1
            if secret_number < key_number:
                print("Type a smaller number next time")
            elif secret_number > key_number:
                print("Type a bigger number next time")
            else:
                t2 = int(time.time())
                print(f"Your guesses: {guesses}")
                print(f"Good work {name}. You got it right in {tries} attempts\n")
                time_[name] = t2 - t1
                return tries, name, points[name]
            if name not in points:
                points[name] = 0
                points[name] = tries
                return tries, name, points[name]
        return None
    except ValueError:
        print("Type a valid number")
