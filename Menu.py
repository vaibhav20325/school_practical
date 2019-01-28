#MENU
game=0
print('Welcome, Which Game do you want to play?')
while game not in [1,2,3]:
    game=int(input('Choose (1) for Stack1e, (2) for TheekThaakToe, (3) for M\'Sweeper: '))

if game==1:
    import main
if game==2:
    import ttt
if game==3:
    
