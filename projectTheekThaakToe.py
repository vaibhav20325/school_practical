#Theek Thaak Toe
import os
import random
#Structure
box1=[['','',''],['','',''],['','','']]
box2=[['','',''],['','',''],['','','']]
box3=[['','',''],['','',''],['','','']]
box4=[['','',''],['','',''],['','','']]
box5=[['','',''],['','',''],['','','']]
box6=[['','',''],['','',''],['','','']]
box7=[['','',''],['','',''],['','','']]
box8=[['','',''],['','',''],['','','']]
box9=[['','',''],['','',''],['','','']]

matrix=[box1,box2,box3,box4,box5,box6,box7,box8,box9]
scoreCard={}
#Defining a function to display the matrix
def display():
    os.system('cls')
    print(21*'--')
    for i in range(0,8,3):
        for j in range (0,3):
            for m in range(0,3):
                print('|',end='')
                for k in range(0,3):
                    if matrix[i+m][j][k]=='':
                        print(matrix[i+m][j][k],end='  |')
                    else:
                        print(matrix[i+m][j][k],end=' |')
                print('\t',end='')
            if j<2:
                print()
                print(21*'- ')
        print()
        print(21*'--')
    print('X: ',list(scoreCard.values()).count('X'),end='\t')
    print('O: ',list(scoreCard.values()).count('O'))
    if num>6:
        box_activated=num-6
    elif num<4:
        box_activated=num+6
    else:
        box_activated=num
    print('Box active is ',box_activated)
      
#Defining a function to check 3 chars in a row
def checkwin(box):
    if (box[0]+box[1]+box[2]).count(char)>=3:
        if box[0][0]==box[0][1]==box[0][2]!='':
            return True
        elif box[1][0]==box[1][1]==box[1][2]!='':
            return True
        elif box[2][0]==box[2][1]==box[2][2]!='':
            return True
        elif box[0][0]==box[1][0]==box[2][0]!='':
            return True
        elif box[0][1]==box[1][1]==box[2][1]!='':
            return True
        elif box[0][2]==box[1][2]==box[2][2]!='':
            return True
        elif box[0][0]==box[1][1]==box[2][2]!='':
            return True
        elif box[0][2]==box[1][1]==box[2][0]!='':
            return True
        else:
            return False
    else:
        return False

def oppChar(str):
    for i in ['X','O']:
        if i != str:
            return i
            break
    
box_no=4
num=5
box_activated=0
turn_no=0
symbol=''
mode=2

print('Hello','\n','Rules: To play press the key on your num pad corresponding to the box. Win 5 boxes to win ')   

while mode not in [0,1]:
    mode=int(input('Press (0) vs computer, (1) vs player, (2) vs AI: '))
    if mode==2:
        print('Still under development')

#Actual GAME

display()

while symbol not in ['X','O']:
    symbol=input('Enter Symbol (X/O): ').upper()

while True:
    if turn_no%2==0:
        char=symbol
    else:
        char=oppChar(symbol)
    
    if mode==0 and turn_no%2 != 0:
        num=random.randint(1,9)
    else:
        try:
            num=int(input('Your chance: '))
        except:
            print('ERROR')
            break
        
    if num not in range(1,10):
        print('Number not within 1 and 9. Try Again')
        continue
    if num in (7,8,9):
        num-=6
    elif num in (1,2,3):
        num+=6

    if matrix[box_no][(num-1)//3][(num-1)%3] =='':
        matrix[box_no][(num-1)//3][(num-1)%3]=char
    elif '' not in matrix[box_no][0]+matrix[box_no][1]+matrix[box_no][2]:
        if list(scoreCard.values()).count(char)>len(scoreCard.values())//2:
            print(char, 'Wins')
        elif list(scoreCard.values()).count(char)==len(scoreCard.values())//2:
            print(oppChar(char), 'Loses')
        else:
            print('Game Tied')
        break
    elif (turn_no%2==0 and mode==0) or mode==1:
        print('Box already occupied')
        continue
    else:
        continue
   
    display()
    if box_no+1 not in scoreCard and checkwin(matrix[box_no]):
        print(char,'Wins this box')
        scoreCard[box_no+1]=char
        if list(scoreCard.values()).count(char)==5:
            print(char,' Wins Congrats')
            break
    box_no=num-1
    turn_no+=1
