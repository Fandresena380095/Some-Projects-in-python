
print("BUBBLE SORT")
num2 = [55456,87,975757,34,987,65546565,98758585,986875754653642,22,2323223,23232332323,224242,444,444,4]

for i in range(len(num2)): 
    for j in range(i+1,len(num2)): #i must be compared to j
        if num2[i] > num2[j]:
            num2[i] ,num2[j] = num2[j] ,num2[i] 
        print(num2)


print(" ")
print("SIMPLIER RESOLUTION")
num3 = [55456,87,975757,34,987,65546565,98758585,986875754653642,22,2323223,23232332323,224242,444,444,4]
num3.sort()
print(num3)


