n=int(input("Enter number of students "))
A=B=C=D=0
for i in range (n):
    age=int(input("Enter Age in years "))
    if age<12:
        D+=1
    elif age<15:
        A+=1
    elif age<17:
        B+=1
    elif age<19:
        C=+1
print ("Group A:",A,"Group B:",B,"Group C:",C,"Group D:",D)
