import q3perfect

running=1
while running:
    try:
        n=int(input('Enter Number:'))
    except:
        break
    try:
        que=int(input("1.See Factors\n2.Check for Prime No\n3."
                      "Check for Perfect No\n"))
    except:
        print('invalid input')
        break
    if que==1:
        print(perfect.Generatefactors(n))
    elif que==2:
        print(perfect.isPrimeNo(n))
    elif que==3:
        print(perfect.isPerfectNo(n))
    else:
        print('Invalid Response')
