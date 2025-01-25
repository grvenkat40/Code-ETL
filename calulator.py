class calculator:
    def add(self,a,b):
        return f'Addition:{a+b}'
    def sub(self,a,b):
        return f'Subtraction:{a-b}'
    def mul(self,a,b):
        return f'Multiplication:{a*b}'
    def div(self,a,b):
        return f'Division:{a/b}'

num=calculator()
while True:
    print("NOTE:If you new this please ")
    print("1.Give new input")
    print("2.Perform operation")
    try:
        op=int(input("Enter your option:\n"))
    except Exception as e:
        print("404 Error!!",e)
    if op==1:
        a=int(input("Enter the n1:"))
        b=int(input("Enter the n2:"))
        user=input("Enter the operation to perform like add,sub,mul,div:")
        if user=="add":
            print(num.add(a,b))
        elif user=='sub':
            print(num.sub(a,b))
        elif user=='mul':
            print(num.mul(a,b))
        elif user=='div':
            print(num.div(a,b))
        else:
            print("Entered wrong!!")
    elif op==2:
        user=input("Enter the operation to perform like add,sub,mul,div:")
        if user=="add":
            print(num.add(a,b))
        elif user=='sub':
            print(num.sub(a,b))
        elif user=='mul':
            print(num.mul(a,b))
        elif user=='div':
            print(num.div(a,b))
        else:
            print("Entered wrong!!")
