import random
import time

points = {}
time_ = {}

def initialize_players(user_number):
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
    for _ in range(user_number):
        tx = "user name " + str(i+1) + ": "
        play = input(tx)
        points[play] = 0
        time_[play] = 0
    return points, time_


