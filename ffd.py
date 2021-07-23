from datetime import datetime

t1 = datetime.now()
x = [
    22,1321,32158,1818,84848,48484,
    45454,6545654,84846,4684,84,684,
    6846848,1212,51151,1515151,515,46,
    4545,841,8419,1841,9841,9841,98
    ]

for i in range(len(x)):
    for j in range(i+1):
        if x[i] < x [j]:
            x[i],x[j] = x[j],x[i]

print(x)
t2 = datetime.now()
t_for_bubble_sort = t2-t1
print(t_for_bubble_sort)


