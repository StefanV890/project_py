import pytest
from unittest.mock import patch
from .ex_game import start_games


points = {}
time_ = {}

def reset_points():
    """fixture to reset the points dictionary before each test."""
    global points
    points = {}
    yield

def test_start_game_correct_guess():
    with patch('random.randint', return_value=50):
        guesses = [30, 40, 50]
        tries, name, attempts = start_games("Stefan", guesses)

        assert tries == 1
        assert name == "Stefan"
        assert attempts == 1


def test_start_game_incorrect_guess():
    with patch('random.randint', return_value=50):
        guesses = [30, 40, 60]
        result = start_games("Stefan", guesses)

        assert result is None
        assert points.get("Stefan", 0) == 0
