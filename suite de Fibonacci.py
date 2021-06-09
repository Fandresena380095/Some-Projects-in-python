#recursive
#value 1 + value 2 = value 3


def linear_fibo():
    n = int(input("Max length : "))
    x = 1
    y = 1
    for i in range(0,n) : #values under the loops are going to be changed
        z = x + y 
        print(y)
        x = y
        y = z
    

linear_fibo()


















