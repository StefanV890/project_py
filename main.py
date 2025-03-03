from game.players import initialize_players, time_, points
from game.game_script import start_game


#def main():
#    try:
#        user_number = int(input("how many users "))
#        player_names = initialize_players(user_number)


#        for player in points.keys():
#            print("")
#            start_game(player)

#        print("RESULTS")
#        for player in points.keys():
#            print(f"{player} - {points[player]} attemps in {time_[player]} seconds")
#    except ValueError:
#        print("Type a number")
#main()
#
#if __name__ == '__main__':
#    main()
i = 0
if __name__ == "__main__":
        user_count = int(input("Enter the number of players: "))
        players = initialize_players(user_count)
        while True:
            i = i+1
            start_game(players)
            if i == user_count:
                break

