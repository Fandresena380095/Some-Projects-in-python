import random

def rec(g):
    x = random.randint(0,g)
    y = random.randint(0,g)
    print("("+str(x)+","+str(y)+")")
    print()
    stop = int(input("Stop :"))
    for i in range(stop):
        print()
        x = y
        delta = random.randint(0,g)
        print("delta : "+ str(delta))
        y = y + delta
        print("x :",x)
        print("y :",y)
        print("x + y ->",x+y)
        
                

rec(7)
        
               
    
