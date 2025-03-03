import random
import time

points = {}
time_ = {}
class Player:
    def __init__(self, name: str):
        self.name = name
        self.attempts = 0
        self.time_taken = 0.0

    def update_score(self, attempts: int, time_taken: float):
        self.attempts = attempts
        self.time_taken = time_taken

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
    players = []
    for i in range(user_number):
        tx = "user name " + str(i+1) + ": "
        play = input(tx)
        points[play] = 0
        time_[play] = 0
    return points, time_, players

