import random
min = 1
max = 6
player1 = 0
val1 = 0
val2 = 0
player2 = 0
roll_again = "da"

while roll_again == "da" or roll_again == "d":
    print ("Valorile pentru player1 sunt:")
    val1 = random.randint(min, max)
    print (val1)
    val2 = random.randint(min, max)
    print (val2)
    zar1 = val1 + val2

    print ("Valorile pentru player2 sunt:")
    val1 = random.randint(min, max)
    print (val1)
    val2 = random.randint(min, max)
    print (val2)
    zar2 = val1 + val2
    if(zar1 > zar2):
        print("Player1 a castigat!")
        player1 = player1 + 1
    else:
        if(zar1 < zar2):
            print("Player2 a castigat!")
            player2 = player2 + 1
        else:
            print("Egal!")
    print ("Scor: player1: ",player1," player2: ",player2)
    roll_again=input('Doriti sa dati cu zarul din nou?')