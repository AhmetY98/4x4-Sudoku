import random
from signal import default_int_handler
#Define global boards
boardX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

board2 = ['1', '2', '3', '4', '5', '6', '7', '8',
            '9', '10', '11', '12', '13', '14', '15', '16']

#Print the board at the start
def printTheBoard(board):
    
    print("\n")
    print("| "+str(board[0])+"  | "+str(board[1]) +
          "  | "+str(board[2])+"  | "+str(board[3])+" |")
    print("----------------------")
    print("| "+str(board[4])+"  | "+str(board[5]) +
          "  | "+str(board[6])+"  | "+str(board[7])+" |")
    print("----------------------")
    print("| "+str(board[8])+"  | "+str(board[9]) +
          " | "+str(board[10])+" | "+str(board[11])+" |")
    print("----------------------")
    print("| "+str(board[12])+" | "+str(board[13]) +
          " | "+str(board[14])+" | "+str(board[15])+" |")
    print("\n")



#print the updated board
def printer(board):

    print("\n")
    print("| "+str(board[0])+"  | "+str(board[1]) +
          "  | "+str(board[2])+"  | "+str(board[3])+" |")
    print("----------------------")
    print("| "+str(board[4])+"  | "+str(board[5]) +
          "  | "+str(board[6])+"  | "+str(board[7])+" |")
    print("----------------------")
    print("| "+str(board[8])+"  | "+str(board[9]) +
          " | "+str(board[10])+" | "+str(board[11])+" |")
    print("----------------------")
    print("| "+str(board[12])+" | "+str(board[13]) +
          " | "+str(board[14])+" | "+str(board[15])+"|")


#Remove the value from the available board
def tempBoard(board, value):    
    board.remove(value)




#Determining who will start first
def determineFirstMove():
    firstMove = random.randint(0, 1)
    if firstMove == 0:
        return 0
    else:
        return 1

#Get user value 
def getElement():

    userNumber = input("Please enter your number: ")

    userNumber = int(userNumber)

    return userNumber


# Replaces the elements in the available board
def replaceElement(replacedElement, board): 
    #finding out if user or computer is X
    global checker
    global starter
    if checker==1:
        user="X"
        computer="O"
    
        if starter == 1:
            indexNumber = replacedElement 
            board[indexNumber-1]=user

        elif starter==0:
            indexNumber = replacedElement
            board[indexNumber-1]=computer

    elif checker==0:
        user="O"
        computer="X"
        if starter==1:
            indexNumber = replacedElement #deleted -1 #Instead of this
            board[indexNumber-1]=user
        elif starter==0:
            indexNumber = replacedElement
            board[indexNumber-1]=computer    
    return board        

    
#Create a random value for computer
def randomIndexCreator(board):
    
    randomNumber=random.choice(board)
    return randomNumber

#Checks if there is a tie
def tieGame(board):

    if len(board) == 0:
        return True
    else:
        return False

#Define winning cases to check from
def winningCases(board):
    input1 = "X"
    input2 = "O"

    # Check rows and columns
##    for i in range(4):
##        if all(board[i * 4 + j] == input1 for j in range(4)) or all(board[i + j * 4] == input1 for j in range(4)):
##            return True
##        elif all(board[i * 4 + j] == input2 for j in range(4)) or all(board[i + j * 4] == input2 for j in range(4)):
##            return True
##
##    # Check diagonals
##    if all(board[i * 5] == input1 for i in range(4)) or all(board[i * 5] == input2 for i in range(4)):
##        return True
##    elif all(board[i * 3 + 3] == input1 for i in range(4)) or all(board[i * 3 + 3] == input2 for i in range(4)):
##        return True
##
##    return False


    if (
            board[0] == input1 and board[1] == input1 and board[2] == input1 and board[4] == input1 or board[4] == input1 and board[5] == input1 and board[6] == input1 and board[7] == input1 or
            board[8] == input1 and board[9] == input1 and board[10] == input1 and board[11] == input1 or board[12] == input1 and board[13] == input1 and board[14] == input1 and board[15] == input1 or
            board[0] == input1 and board[4] == input1 and board[8] == input1 and board[12] == input1 or board[1] == input1 and board[5] == input1 and board[9] == input1 and board[13] == input1 or
            board[2] == input1 and board[6] == input1 and board[10] == input1 and board[14] == input1 or board[3] == input1 and board[7] == input1 and board[11] == input1 and board[15] == input1 or
            board[0] == input1 and board[5] == input1 and board[10] == input1 and board[15] == input1 or board[3] == input1 and board[6] == input1 and board[9] == input1 and board[12] == input1 or
            board[1] == input1 and board[6] == input1 and board[11] == input1 or board[2] == input1 and board[5] == input1 and board[8] == input1 or board[4] == input1 and board[9] == input1 and board[14] == input1 or
            board[7] == input1 and board[10] == input1 and board[13] == input1):

        return True
    elif (board[0] == input2 and board[1] == input2 and board[2] == input2 and board[4] == input2 or board[4] == input2 and board[5] == input2 and board[6] == input2 and board[7] == input2 or
          board[8] == input2 and board[9] == input2 and board[10] == input2 and board[11] == input2 or board[12] == input2 and board[13] == input2 and board[14] == input2 and board[15] == input2 or
          board[0] == input2 and board[4] == input2 and board[8] == input2 and board[12] == input2 or board[1] == input2 and board[5] == input2 and board[9] == input2 and board[13] == input2 or
          board[2] == input2 and board[6] == input2 and board[10] == input2 and board[14] == input2 or board[3] == input2 and board[7] == input2 and board[11] == input2 and board[15] == input2 or
          board[0] == input2 and board[5] == input2 and board[10] == input2 and board[15] == input2 or board[3] == input2 and board[6] == input2 and board[9] == input2 and board[12] == input2 or
          board[1] == input2 and board[6] == input2 and board[11] == input2 or board[2] == input2 and board[5] == input2 and board[8] == input2 or board[4] == input2 and board[9] == input2 and board[14] == input2 or
          board[7] == input2 and board[10] == input2 and board[13] == input2):
        return True
    else:
        return False

#state a number for turns
starter = determineFirstMove()
checker=starter

class ComputerPlayType:
    def __init__(self,symbol,difficulty):
        self.symbol=symbol # Either X or O
        self.difficulty=difficulty

    def make_move(self,board):
        _,move=self.minimax(board,self.symbol,depth_level=self.difficulty) #assigining the move to the symbol
        return move
    def minimax(self,board, gamer, depth_level):
        #checking available moves by looking at the values if they are number or not
        available_moves=[i for i, value in enumerate(board) if value.isdigit()]

        if(winningCases(board)):
            if gamer == self.symbol:
                return -1,None #let the player win
            else:
                return 1,None #let the computer win
        elif tieGame(board):
            return 0,None #The game is a tie


        #To check which depth we are at we need a depth limit
        if depth_level==0:
            return 0,None #when the depth level reaches 0 we will send neutral score

        #To maximize the computer score
        if gamer==self.symbol:
            best_score=float('-inf')
            best_move=None
            for move in available_moves:
                new_board=board.copy()
                new_board[move]=player
                score , _ =self.minimax(new_board,"X" if gamer=="O" else "O",depth_level-1)
                if score>best_score:
                    best_score=score
                    best_move=move
            return best_score,best_move
            
        #To minimize the player score
        else:
            best_score=float('inf')
            best_move=None
            for move in available_moves:
                new_board=board.copy()
                new_board[move]=gamer
                score,_=self.minimax(new_board,"X" if gamer=="O" else "O",depth_level-1)
                if score< best_score:
                    best_score=score
                    best_move=move
            return best_score,best_move
            

           

def main():
    global starter
    
    printTheBoard(board2)
    conditionWinning = winningCases(board2)
    noWinner=True

    #ask for difficutly
    difficulty=input("Choose the difficulty level by entering easy, medium or hard (will be medium if nothing is entered): ")
    difficulty_level={"easy":1,"medium":3,"hard":5}
    depth_level=difficulty_level.get(difficulty.lower(),3)

    computer_player=ComputerPlayType("O" if checker==1 else "X",depth_level)
    
    
    if len(boardX) != 0 and noWinner == True:
        while noWinner == True:
            i = starter
            if i==1:
                print("Your Turn")
            else:
                print("Computer's Turn")
            if i == 1:  
                userX = getElement()
                userXstring = str(userX)
                if userXstring in board2:
                    newList = replaceElement(
                        userX, board2)  # create a new list
                    printer(newList)
                    tempBoard(boardX, userX) # pop the value
                    starter = 0 
                    conditionWinning = winningCases(board2)
                    if conditionWinning==True:
                        noWinner=False
                        print("You won!")
                        break
                     
                    
            elif i == 0:  # else starter==1
                newValue = randomIndexCreator(boardX)  #Create a computer value
                randomValue = str(newValue)   
                if randomValue not in board2: 
                        newValue=randomIndexCreator(boardX)
                        randomValue=str(newValue)
                
                #Check if the computer generated value is in list        
                while noWinner==True and starter!=1: 
                    
                    if randomValue in board2:
                        newList = replaceElement(newValue, board2)
                        printer(newList)
                        tempBoard(boardX, newValue) # pop the value
                        starter = 0 
                        if conditionWinning==True:
                            noWinner=False
                            print("Computer Won!")
                            break
                        starter = 1
                    elif randomValue not in board2:
                         newValue=randomIndexCreator(boardX)
                         randomValue=str(newValue)
                         break
                    elif tieGame(boardX)==True:
                        print("The game is a tie")
                        noWinner=False
                        break                
    
                            
main()
