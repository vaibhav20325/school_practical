def validPassword(l):
    valid=[]
    for pword in l:
        d={'int':[],'let_s':[],'sp':[],'let_b':[]}
        validity=True
        chars=list(pword)
        for i in chars:
            if i.isalpha():
                if i.islower():
                    d['let_s'].append(i)
                else:
                    d['let_b'].append(i)
            elif i.isdigit():
                d['int'].append(i)
            elif i in '$#@':
                d['sp'].append(i)
            else:
                validity=False
        for i in d:
            if d[i]==[]:
                validity=False
        if validity==True:
            valid.append(pword)
    print('Valid Passwords:', valid)
l=eval(input('Enter list of passwords:'))
validPassword(l)
