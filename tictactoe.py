import os, random, time
os.system("title Tic Tac Toe Python")

def main(playermove):
    game = True
    filled = 0
    row1, row2, row3 = resetboard()
    while game:
        os.system("cls")
        print("   1   2   3")
        print("1  "+row1[0]+" | "+row1[1]+" | "+row1[2])
        print("2  "+row2[0]+" | "+row2[1]+" | "+row2[2])
        print("3  "+row3[0]+" | "+row3[1]+" | "+row3[2]+"\n")
        if playermove == True:
            row = int(input("Select Row #: "))
            if row != 1 and row != 2 and row != 3:
                print("\nPlease select 1,2, or 3!")
                time.sleep(2)
                continue
            rownum = row
            if row == 1:
                row = row1
            elif row == 2:
                row = row2
            else:
                row = row3
            counter = 0
            for i in range(rownum):
                i -= 1
                if row[i] != " ":
                    counter += 1
            if counter == 3:
                print("\nPlease select an unfilled row!")
                time.sleep(2)
                continue
            col = int(input("Select Column #: "))
            if col != 1 and col != 2 and col != 3:
                print("\nPlease select 1,2, or 3!")
                time.sleep(2)
                continue
            if row[col-1] != " ":
                print("\nPlease select a unfilled spot!")
                time.sleep(2)
                continue
            row[col-1] = "X"
            playermove = False
            filled += 1
        else:
            if row1[0] == "X" and row1[1] == "X" and row1[2] == " ":
                row1[2] = "O"
            elif row2[0] == "X" and row2[1] == "X" and row2[2] == " ":
                row2[2] = "O"
            elif row3[0] == "X" and row3[1] == "X" and row3[2] == " ":
                row3[2] = "O"
            elif row1[1] == "X" and row1[2] == "X" and row1[0] == " ":
                row1[0] = "O"
            elif row2[1] == "X" and row2[2] == "X" and row2[0] == " ":
                row2[0] = "O"
            elif row3[1] == "X" and row3[2] == "X" and row3[0] == " ":
                row3[0] = "O"
            elif row1[0] == "X" and row2[0] == "X" and row3[0] == " ":
                row3[0] = "O"
            elif row1[1] == "X" and row2[1] == "X" and row3[1] == " ":
                row3[1] = "O"
            elif row1[2] == "X" and row2[2] == "X" and row3[2] == " ":
                row3[2] = "O"
            elif row3[0] == "X" and row2[0] == "X" and row1[0] == " ":
                row1[0] = "O"
            elif row3[1] == "X" and row2[1] == "X" and row1[1] == " ":
                row1[1] = "O"
            elif row3[2] == "X" and row2[2] == "X" and row1[2] == " ":
                row1[2] = "O"
            elif row1[0] == "X" and row2[1] == "X" and row3[2] == " ":
                row3[2] = "O"
            elif row2[1] == "X" and row3[2] == "X" and row1[0] == " ":
                row1[0] = "O"
            elif row1[2] == "X" and row2[1] == "X" and row3[0] == " ":
                row3[0] = "O"
            elif row3[0] == "X" and row2[1] == "X" and row1[2] == " ":
                row1[0] = "O"
            elif row1[0] == "X" and row1[2] == "X" and row1[1] == " ":
                row1[1] = "O"
            elif row2[0] == "X" and row2[2] == "X" and row2[1] == " ":
                row2[1] = "O"
            elif row3[0] == "X" and row3[2] == "X" and row3[1] == " ":
                row3[1] = "O"
            elif row1[0] == "X" and row3[0] == "X" and row2[0] == " ":
                row2[0] = "O"
            elif row1[1] == "X" and row3[1] == "X" and row2[1] == " ":
                row2[1] = "O"
            elif row1[2] == "X" and row3[2] == "X" and row2[2] == " ":
                row2[2] = "O"
            else:
                looking = True
                if row2[1] == " ":
                    chance = random.randint(1,2)
                    if chance == 1:
                        row2[1] = "O"
                        looking = False
                while looking:
                    row = random.randint(1,3)
                    col = random.randint(0,2)
                    if row == 1:
                        row_ = row1
                    elif row == 2:
                        row_ = row2
                    else:
                        row_ = row3
                    if row_[col] == " ":
                        row_[col] = "O"
                        looking = False
            filled += 1
            playermove = True
        if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
            return "Player"
        elif row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
            return "Player"
        elif row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
            return "Player"
        elif row1[1] == "X" and row1[2] == "X" and row1[0] == "X":
            return "Player"
        elif row2[1] == "X" and row2[2] == "X" and row2[0] == "X":
            return "Player"
        elif row3[1] == "X" and row3[2] == "X" and row3[0] == "X":
            return "Player"
        elif row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
            return "Player"
        elif row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
            return "Player"
        elif row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
            return "Player"
        elif row3[0] == "X" and row2[0] == "X" and row1[0] == "X":
            return "Player"
        elif row3[1] == "X" and row2[1] == "X" and row1[1] == "X":
            return "Player"
        elif row3[2] == "X" and row2[2] == "X" and row1[2] == "X":
            return "Player"
        elif row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
            return "Player"
        elif row2[1] == "X" and row3[2] == "X" and row1[0] == "X":
            return "Player"
        elif row1[2] == "X" and row2[1] == "X" and row3[0] == "X":
            return "Player"
        elif row3[2] == "X" and row2[1] == "X" and row1[0] == "X":
            return "Player"
        elif row1[0] == "X" and row1[2] == "X" and row1[1] == "X":
            return "Player"
        elif row2[0] == "X" and row2[2] == "X" and row2[1] == "X":
            return "Player"
        elif row3[0] == "X" and row3[2] == "X" and row3[1] == "X":
            return "Player"
        elif row1[0] == "X" and row3[0] == "X" and row2[0] == "X":
            return "Player"
        elif row1[1] == "X" and row3[1] == "X" and row2[1] == "X":
            return "Player"
        elif row1[2] == "X" and row3[2] == "X" and row2[2] == "X":
            return "Player"
        elif row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
            return "Bot"
        elif row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
            return "Bot"
        elif row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
            return "Bot"
        elif row1[1] == "O" and row1[2] == "O" and row1[0] == "O":
            return "Bot"
        elif row2[1] == "O" and row2[2] == "O" and row2[0] == "O":
            return "Bot"
        elif row3[1] == "O" and row3[2] == "O" and row3[0] == "O":
            return "Bot"
        elif row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
            return "Bot"
        elif row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
            return "Bot"
        elif row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
            return "Bot"
        elif row3[0] == "O" and row2[0] == "O" and row1[0] == "O":
            return "Bot"
        elif row3[1] == "O" and row2[1] == "O" and row1[1] == "O":
            return "Bot"
        elif row3[2] == "O" and row2[2] == "O" and row1[2] == "O":
            return "Bot"
        elif row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
            return "Bot"
        elif row2[1] == "O" and row3[2] == "O" and row1[0] == "O":
            return "Bot"
        elif row1[2] == "O" and row2[1] == "O" and row3[0] == "O":
            return "Bot"
        elif row3[2] == "O" and row2[1] == "O" and row1[0] == "O":
            return "Bot"
        elif row1[0] == "O" and row1[2] == "O" and row1[1] == "O":
            return "Bot"
        elif row2[0] == "O" and row2[2] == "O" and row2[1] == "O":
            return "Bot"
        elif row3[0] == "O" and row3[2] == "O" and row3[1] == "O":
            return "Bot"
        elif row1[0] == "O" and row3[0] == "O" and row2[0] == "O":
            return "Bot"
        elif row1[1] == "O" and row3[1] == "O" and row2[1] == "O":
            return "Bot"
        elif row1[2] == "O" and row3[2] == "O" and row2[2] == "O":
            return "Bot"
        elif filled == 9:
            return "Tie"
        

def resetboard():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    
def startgame():
    os.system("cls")
    choice = input("heads or tails?: ")
    choice = choice.lower()
    if choice != "heads" and choice != "tails":
        os.system("cls")
        print("Please enter heads or tails!")
        time.sleep(2)
        startgame()
    coinflip = random.randint(1,2)
    if choice == "heads":
        value = 1
    else:
        value = 2
    os.system("cls")
    if value == coinflip:
        print("You have won the coinflip!")
        playermove = True
    else:
        print("You have lost the coinflip :(")
        playermove = False
    time.sleep(2)
    winner = main(playermove)
    if winner == "Player":
        os.system("cls")
        print("You have won!")
    elif winner == "Bot":
        os.system("cls")
        print("You have lost :(")
    else:
        os.system("cls")
        print("Draw!")
    waitresponse = True
    while waitresponse:
        playagain = str(input("Play again? (yes/no): "))
        playagain = playagain.lower()
        if playagain == "yes":
            startgame()
        elif playagain == "no":
            quit()
        else:
            continue
        
    
print("""
Press Enter to Play
""")
input("")
startgame()
