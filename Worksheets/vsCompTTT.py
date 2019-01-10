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
    
print('Hello','\n','Rules: To play press the key on your num pad corresponding to the box')   
display()
box_no=4
turn_no=0

#Actual GAME
while True:
    if turn_no%2==0:
        char='X'
    else:
        char='O'
    if turn_no%2==0:
        try:
            num=int(input('Your chance '))
        except:
            print('ERROR')
            break
    else:
        num=random.randint(1,9)

    if num not in range(1,10):
        print('Number not within 1 and 9. Try Again')
        continue
    if num in (7,8,9):
        num-=6
    elif num in (1,2,3):
        num+=6

    if matrix[box_no][(num-1)//3][(num-1)%3] =='':
        matrix[box_no][(num-1)//3][(num-1)%3]=char
    elif '' not in matrix[box_no][0]+matrix[box_no][0]+matrix[box_no][0]:
        if list(scoreCard.values()).count(char)>len(scoreCard.values())//2:
            print(char, 'Wins')
        elif list(scoreCard.values()).count(char)=len(scoreCard.values())//2:
            print(char, 'Loses')
        else:
            print('Game Tied')
    elif turn_no%2==0:
        print('Box already occupied')
        continue
    else:
        continue
    if turn_no%2!=0:
        display()    
    if box_no+1 not in scoreCard and checkwin(matrix[box_no]):
        print(char,'Wins this box')
        scoreCard[box_no+1]=char
        if list(scoreCard.values()).count(char)==5:
            print(char,' Wins Congrats')
            break
    box_no=num-1
    turn_no+=1
