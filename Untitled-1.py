a = input('How many option do you want to choose: ')

d ={1:'c' , 2:'python' ,3:'java'}

for i in range(int(a)):
    x = input(' Press your desired programming language in valid name :' )
    def choice(x):
        if x == d[1] or x == d[2] or x == d[3]:
            
            return  x


    print(choice(x))
