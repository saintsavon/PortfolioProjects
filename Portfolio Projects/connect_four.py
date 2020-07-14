import random

user_chose_pos = []
player1_chose_pos = []
player2_chose_pos = []

computer_pos = ["01", "02", "03", "04", "05", "06", "07",
                "08", "09", "10", "11", "12", "13", "14",
                "15", "16", "17", "18", "19", "20", "21",
                "22", "23", "24", "25", "26", "27", "28",
                "29", "30", "31", "32", "33", "34", "35",
                "36", "37", "38", "39", "40", "41", "42",]

def displayBoard():
        print("Player 1 will be: 'X'\nPlayer 2 will be: 'O'")
        print("Here is the board:\n")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")
        print("|     |     |     |     |     |     |     |")
        print("-------------------------------------------")

def boardView():
    pos01 = pos02 = pos03 = pos04 = pos05 = pos06 = pos07 = "-"
    pos08 = pos09 = pos10 = pos11 = pos12 = pos13 = pos14 = "-"
    pos15 = pos16 = pos17 = pos18 = pos19 = pos20 = pos21 = "-"
    pos22 = pos23 = pos24 = pos25 = pos26 = pos27 = pos28 = "-"
    pos29 = pos30 = pos31 = pos32 = pos33 = pos34 = pos35 = "-"
    pos36 = pos37 = pos38 = pos39 = pos40 = pos41 = pos42 = "-"

    for i in player1_chose_pos:
        if i == "42":
            pos42 = "X"
        elif i == "41":
            pos41 = "X"

    for i in player2_chose_pos:
        if i == "42":
            pos42 = "O"
        elif i == "41":
            pos41 = "O"