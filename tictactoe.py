from copy import deepcopy
from random import choice
import math

def printGrid(grid):
    print("-------------")
    for i in range(3):
        for j in range(3):
            if grid[i][j] == None:
                print("|  ",end=" ")
            else:
                print("|",grid[i][j],end=" ")
        print("|",end="")
        print()
        print("-------------")
    

def max_valueX(state,move,player):
    if terminal(state,move):
        u_val = utility(state, move, player)
        return [u_val,None]
    v = -math.inf
    best_move = None;
    for action in actions(state):
        val = min_valueX(deepcopy(result(state,action,move)),"O",player)[0]
        if val > v:
            v = val;
            best_move = action
    return [v,best_move]

def min_valueX(state,move,player):
    if terminal(state,move):
        u_val = utility(state, move, player)
        return [u_val,None]
    v = math.inf
    best_move = None;
    for action in actions(state):
        val = max_valueX(deepcopy(result(state,action,move)),"X",player)[0]
        if val < v:
            v = val;
            best_move = action
    return [v,best_move]

def max_valueO(state,move,player):
    if terminal(state,move):
        u_val = utility(state, move, player)
        return [u_val,None]
    v = -math.inf
    best_move = None;
    for action in actions(state):
        val = min_valueO(deepcopy(result(state,action,move)),"X",player)[0]
        if val > v:
            v = val;
            best_move = action
    return [v,best_move]

def min_valueO(state,move,player):
    if terminal(state,move):
        u_val = utility(state, move, player)
        return [u_val,None]
    v = math.inf
    best_move = None;
    for action in actions(state):
        val = max_valueO(deepcopy(result(state,action,move)),"O",player)[0]
        if val < v:
            v = val;
            best_move = action
    return [v,best_move]




def minimaxAlgo(state,move,player):
    if move == "O":
        bestmove = max_valueO(state, move, player)[1]
    else:
        bestmove = max_valueX(state, move, player)[1]
    return bestmove


def checkRows(grid,move):
    if grid[0][0] == move and grid[0][1] == move and grid[0][2] == move:
        return True
    if grid[1][0] == move and grid[1][1] == move and grid[1][2] == move: 
        return True
    if grid[2][0] == move and grid[2][1] == move and  grid[2][2] == move:
        return True
    return False

def checkCol(grid,move):
    if grid[0][0] == move and grid[1][0] == move and grid[2][0] == move:
        return True
    if grid[0][1] == move and grid[1][1] == move and grid[2][1] == move:
        return True
    if grid[0][2] == move and grid[1][2] == move and grid[2][2] == move:
        return True
    return False

def checkDiag(grid,move):
    if grid[0][0] == move and grid[1][1] == move and grid[2][2] == move:
        return True
    if grid[0][2] == move and  grid[1][1] == move and grid[2][0] == move:
        return True
    return False

def checkDraw(grid,move):
    flag = False
    
    if checkCol(grid,move) or checkRows(grid,move) or checkDiag(grid,move):
        return  False;

    for i in range(3):
        for j in range(3):
            if grid[i][j] == None:
                flag = True
                break
    if flag == False:
        return True
    else:
        return False

def terminal(grid,move):
    if checkCol(grid,move) or checkRows(grid,move) or checkDiag(grid,move):
        return  True;
    elif checkDraw(grid,move):
        return True
    else:
        return False        


def player(turn):
   if turn == None :
       return "X"
   if turn == "X":
       return "O"
   elif turn == "O":
       return "X"

def utility(state,move,player):
    if player[move] == "cpu" and  terminal(state,move) == True and checkDraw(state,move) == False:
        return 1;
    if player[move] == "human" and  terminal(state,move) == True and checkDraw(state,move) == False:
        return -1;
    if terminal(state,move) == True and  checkDraw(state,move) == True:
        return 0;

def actions(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == None:
                moves.append((i,j))
    return moves

def result(state,action,move):
    state = deepcopy(state)
    x,y = action;
    state[x][y] = move;
    return state;



def validMove(grid,move):
    valid = True
    if move.isdigit() == False:
        return False
    else:
        move = int(move)
        if move < 1 or move > 9:
            valid = False
        count = 1
        for i in range(3):
            for j in range(3):
                if move == count:
                    if grid[i][j] is not None:
                        valid = False
                count += 1
    
    return valid
    

def gameVsPlayer(grid):
    currTurn = None
    players = {}
    gameOver = False
    ngrid = deepcopy(grid)
    while True:
        if gameOver:
            break
        print()
        print("Select move option for player 1 :");
        print("1.X");
        print("2.O");
        opt = input("Enter a number(1-2):")
        if opt.isdigit() == False:
            print("Not a valid option")
            print()
            break
        else:
            opt = int(opt)
            if opt == 1:
                players['X'] = "p1"
                players['O'] = "p2"
                print("Player 1 will play X Player 2 will play O")
            elif opt == 2:
                players['O'] = "p1"
                players['X'] = "p2"
                print("Player 2 will play X Player 2 will play O")
            else:
                print("Not a valid option")
                print()
                break
        while True:
            print()
            printGrid(ngrid)
            print()
            currTurn = player(currTurn)
            if currTurn == "X":
                m = input("Enter a move for player X (1-9) : ")
                if validMove(ngrid, m):
                    m = int(m)
                    count = 1
                    for i in range(3):
                        for j in range(3):
                            if m == count:
                                ngrid[i][j] = "X"
                            count += 1
                    if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn)  == False:
                        print();
                        printGrid(ngrid)
                        print()
                        print(players[currTurn] + " won the game")
                        gameOver = True
                        break;
                    elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn)  == True :
                        print()
                        printGrid(ngrid)
                        print()
                        print("Game is draw")
                        gameOver = True
                        break;
                else:
                    print("Invalid move")
                    currTurn = "O"
                    print()
            else:
                m = input("Enter a move for player O (1-9) : ")
                if validMove(ngrid, m):
                    m = int(m)
                    count = 1
                    for i in range(3):
                        for j in range(3):
                            if m == count:
                                ngrid[i][j] = "O"
                            count += 1
                    if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn) == False:
                        print();
                        printGrid(ngrid)
                        print()
                        print(players[currTurn] + " won the game")
                        gameOver = True
                        break;
                    elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn) == True :
                        print()
                        printGrid(ngrid)
                        print()
                        print("Game is draw")
                        gameOver = True
                        break;
                else:
                    print("Invalid move")
                    currTurn = "X"
                    print()
        

def gameVsComputer(grid):
    currTurn = None
    players = {}
    gameOver = False
    ngrid = deepcopy(grid)
    while True:
        if gameOver:
            break
        print()
        print("Select move option for human player :");
        print("1.X");
        print("2.O");
        opt = input("Enter a number(1-2):")
        if opt.isdigit() == False:
            print("Not a valid option")
            print()
            break
        else:
            opt = int(opt)
            if opt == 1:
                players['X'] = "human"
                players['O'] = "cpu"
                print("Human will play X CPU will play O")
            elif opt == 2:
                players['O'] = "human"
                players['X'] = "cpu"
                x = choice([0,1,2])
                y = choice([0,1,2])
                ngrid[x][y] = "X"
                currTurn = "X"
                print("CPU will play X Human will play O")
            else:
                print("Not a valid option")
                print()
                break
        while True:
            printGrid(ngrid)
            print()
            currTurn = player(currTurn)
            if currTurn == "X" and players[currTurn] == "cpu":
               act = minimaxAlgo(ngrid, currTurn, players)
               x,y = act;
               ngrid[x][y] = "X";
               print("CPU placed move at row,col =",x,",",y);
               if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn) == False:
                   print();
                   printGrid(ngrid)
                   print()
                   print(players[currTurn] + " won the game")
                   gameOver = True
                   break;
               elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn) == True :
                   print()
                   printGrid(ngrid)
                   print()
                   print("Game is draw")
                   gameOver = True
                   break;
            elif currTurn == "O" and players[currTurn] == "human":
                m = input("Enter a move for player O (1-9) : ")
                if validMove(ngrid, m):
                    m = int(m)
                    count = 1
                    for i in range(3):
                        for j in range(3):
                            if m == count:
                                ngrid[i][j] = "O"
                            count += 1
                    if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn) == False:
                        print();
                        printGrid(ngrid)
                        print()
                        print(players[currTurn] + " won the game")
                        gameOver = True
                        break;
                    elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn) == True :
                        print()
                        printGrid(ngrid)
                        print()
                        print("Game is draw")
                        gameOver = True
                        break;
                else:
                    print("Invalid move")
                    currTurn = "X"
                    print()
            elif currTurn == "O" and players[currTurn] == "cpu":
                act = minimaxAlgo(ngrid, currTurn, players)
                x,y = act;
                ngrid[x][y] = "O";
                print("CPU placed move at row,col =",x,",",y);
                if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn) == False:
                    print();
                    printGrid(ngrid)
                    print()
                    print(players[currTurn] + " won the game")
                    gameOver = True
                    break;
                elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn) == True :
                    print()
                    printGrid(ngrid)
                    print()
                    print("Game is draw")
                    gameOver = True
                    break;
            else:
                m = input("Enter a move for player X (1-9) : ")
                if validMove(ngrid, m):
                    m = int(m)
                    count = 1
                    for i in range(3):
                        for j in range(3):
                            if m == count:
                                ngrid[i][j] = "X"
                            count += 1
                    if terminal(ngrid,currTurn) == True and checkDraw(ngrid,currTurn) == False:
                        print();
                        printGrid(ngrid)
                        print()
                        print(players[currTurn] + " won the game")
                        gameOver = True
                        break;
                    elif terminal(ngrid,currTurn) == True  and checkDraw(ngrid,currTurn) == True :
                        print()
                        printGrid(ngrid)
                        print()
                        print("Game is draw")
                        gameOver = True
                        break;
                else:
                    print("Invalid move")
                    currTurn = "O"
                    print()
                
                

def main():
    
    grid = [[None for i in range(3)] for j in range(3)]
    
    print("TIC TAC TOE");
    print();
    while True:
        print("Select an option :")
        print("1. Vs Player")
        print("2. Vs Computer")
        print("3. Exit")
        
        opt = input("Enter a number(1-3):")
        if opt.isdigit() == False:
            print("Not a valid option")
            print()
        else:
            opt = int(opt)
            if opt == 1:
                gameVsPlayer(grid)
            elif opt == 2:
                gameVsComputer(grid)
            elif opt == 3:
                break
            else:
                print("Invalid Option")
                print()
        

main()

