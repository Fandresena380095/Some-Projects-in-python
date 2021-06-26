'''
You will have to pick a number between 1 and 10
You have 3 guesses
'''
import random



#this is a fairly linear indented approach of the random game
print("guess a number between 1 and 10")
x = random.randint(1, 10)
g = 1
print(x)

    
while g<3 :
    import verifyModule
    try1In = int(input("guess 1/3: "))
    try1 = verifyModule.verify(try1In)
    if try1 == x:
        print("Well done!that was fast")
        break
    else :
        g+=1
        print("Oups, try again")
        print("it is between", random.randint(x-3,x) ,'and', random.randint(x,x+3))
        try2In = int(input("guess 2/3: "))
        try2 = verifyModule.verify(try2In)
        if try2 == x:
            print("Well done!")
            break
        else :
            g+=1
            print("Oups, try again")
            print("it is between", random.randint(x-2,x) ,'and', random.randint(x,x+2))
            try3In = int(input("guess 3/3: "))
            try3 = verifyModule.verify(try3In)
            if try3 == x:
                print("Well done!Borderline")
            else :
                g+=1
                print("You lose")

        
