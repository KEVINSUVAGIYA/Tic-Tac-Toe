def Board(pattern):
    print("Current State :\n\n")
    for i in range(0, 9):
        if ((i > 0) and (i % 3 == 0)):
            print("\n")
        if (pattern[i] == 0):
            print("_ ", end=" ")
        if (pattern[i] == -1):
            print("X ", end=" ")
        if (pattern[i] == 1):
            print("O ", end=" ")
    print("\n\n")


def Player1Turn(pattern):
    position = int(input("Enter X's position from [1,2,3,4,5,6,7,8,9] : "))
    if (pattern[position-1] != 0):
        print("Invalid Move!")
        exit(0)
    pattern[position-1] = -1


def Player2Turn(pattern):
    position = int(input("Enter O's position from [1,2,3,4,5,6,7,8,9] : "))
    if (pattern[position-1] != 0):
        print("Invalid Move!")
        exit(0)
    pattern[position-1] = 1


def analyse(pattern, player):
    x = CurrentState(pattern)
    if (x != 0):
        return (x*player)
    position = -1
    value = -2
    for i in range(0, 9):
        if (pattern[i] == 0):
            pattern[i] = player
            score = -analyse(pattern, player*-1)
            pattern[i] = 0
            if (score > value):
                value = score
                position = i
    if (position == -1):
        return 0
    return value


def CompTurn(pattern):
    position = -1
    value = -2
    for i in range(0, 9):
        if (pattern[i] == 0):
            pattern[i] = 1
            score = -analyse(pattern, -1)
            pattern[i] = 0
            if (score > value):
                value = score
                position = i
    pattern[position] = 1


def CurrentState(pattern):
    winPatern = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (pattern[winPatern[i][0]] != 0 and pattern[winPatern[i][0]] == pattern[winPatern[i][1]] and pattern[winPatern[i][0]] == pattern[winPatern[i][2]]):
            return pattern[winPatern[i][2]]
    return 0


def main():
    choice = int(input("1. Single Player\n2. MultiPlayer : "))
    pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (choice == 1):
        print("Computer: 0 Vs. You: X")
        player = int(input("1. First Turn \n 2. Second Turn : "))
        for i in range(0, 9):
            if (CurrentState(pattern) != 0):
                break
            if ((i+player) % 2 == 0):
                CompTurn(pattern)
            else:
                Board(pattern)
                Player1Turn(pattern)
    else:
        for i in range(0, 9):
            if (CurrentState(pattern) != 0):
                break
            if ((i) % 2 == 0):
                Board(pattern)
                Player1Turn(pattern)
            else:
                Board(pattern)
                Player2Turn(pattern)

    x = CurrentState(pattern)
    if (x == 0):
        Board(pattern)
        print("Draw!")
    elif (x == -1):
        Board(pattern)
        print("X wins !")
    elif (x == 1):
        Board(pattern)
        print("O wins !")

main()