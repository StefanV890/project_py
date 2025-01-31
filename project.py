import random

punctaj={}

def start_game(name):
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
            print("your guesses are ", guesses )
            print("good work ",name,". You got it right in", tries,"attemps")
            print("")
            punctaj[name]=tries
            break

user_number =int(input("how many users "))
for i in range(user_number):
    tx = "user name " + str(i+1) + ": "
    a = input(tx)
    punctaj[a]=0

for i in punctaj.keys():
    print("")
    start_game(i)

print("RESULTS")
for i in punctaj.keys():
    print(i,"  -  ",punctaj[i]," attemps")


"""
cati playeri sunt (player1:nume player2:nume) start player, start player2...
mantin playeri si 

"""