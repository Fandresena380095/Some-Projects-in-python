import random

def rec(g):
    x = 1
    y = 1
    stop = int(input("Stop :"))
    for i in range(stop):
        print()
        x = y
        y = y + random.randint(0,g)
        print("("+str(x)+","+str(y)+")")
        print("x + y ->",x+y)
                        

rec(7)
