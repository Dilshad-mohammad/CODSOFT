'''
ROCK-PAPER-SCISSOR GAME...

Rules:
Rock wins against Scissors
Scissor wins against Paper
Paper wins agaist Rock.
'''
import random
play = True
while play:
    Game = int(input('''
Start Game...
1 YES
2 NO/EXIT'''))
    if Game == 1:
        for i in range(9):
            user = int(input("Your Turn:\nPress 0 for Rock\nPress 1 for Scissor\nPress 2 for Paper\n"))
            Computer = random.randint(0,2)        
            if user == 0:
                print("\t\tYou Chose: Rock")
            elif user == 1:
                print("\t\tYou Chose: Scissor")
            elif user == 2:
                print("\t\tYou Chose: Paper")
            else:
                print("\t\tEnter Valid Number")
                break
            if user == 1 or 2 or 3:
                if Computer == 0:
                    print("\t\tComputer Chose: Rock")
                elif Computer == 1:
                    print("\t\tComputer Chose: Scissor")
                elif Computer == 2:
                    print("\t\tComputer Chose: Paper")
            else:
                break
            if Computer == user:
                print("\t\tIT'S A TIE")            
            elif user == 0 and Computer == 1:
                print("\t\tYOU WIN")
            elif user == 0 and Computer == 2:
                print("\t\tYOU LOSE")
            elif user == 1 and Computer == 0:
                print("\t\tYOU LOSE")
            elif user == 1 and Computer == 2:
                print("\t\tYOU WIN")
            elif user == 2 and Computer == 0:
                print("\t\tYOU WIN")
            elif user == 2 and Computer == 1:
                print("\t\tYOU LOSE")
    if Game == 2:
        play = False
        print("SEE YOU SOON!")

            
