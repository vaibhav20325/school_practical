class Stack():
    def __init__(self):
        self.s=[]
    def push(self,a):
        self.s.append(a)
    def pop(self):
        if len(self.s)>0:
            return self.s.pop()
        else:
            return False
    def peek(self):
        if len(self.s)>0:
            return self.s[-1]
        else:
            return False
stack=Stack()
temp_stack=Stack()  
n=int(input('Enter Number Of Rings: '))
for i in range(n):
    d=int(input('Enter Diameter: '))
    if len(stack.s)==0 or d>=stack.peek():
        stack.push(d)
    elif d<stack.peek():
        while len(stack.s)>0 and d<=stack.peek():
            temp_stack.push(stack.pop())
        stack.push(d)
        while len(temp_stack.s):
            stack.push(temp_stack.pop())
    print('The Ring Stand: ',stack.s)
    
    
