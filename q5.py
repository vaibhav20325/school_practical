def base_convert(i,base):
    if i<base:
        if i>9:
            return chr(ord('A')+i%10)
        else:
            return i
    else:
        return str(base_convert(i//base,base))+str(i%base)
    
num=int(input('Enter Number in Decimal: '))
base=input('Desired Base (B for Binary, O for Octal, H for Hexadecimal): ')

d={'b':2,'o':8,'h':16}
try:
    base = d[base.lower()]
except:
    base=int(base)

print(base_convert(num,base))
        
