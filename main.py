from game.players import initialize_players, time_, points
from game.game_script import start_game


def main():
    try:
        user_number = int(input("how many users "))
        initialize_players(user_number)

        for player in points.keys():
            print("")
            start_game(player)

        print("RESULTS")
        for player in points.keys():
            print(f"{player} - {points[player]} attemps in {time_[player]} seconds")
    except ValueError:
        print("Type a number")
main()

if __name__ == '__main__':
    main()

