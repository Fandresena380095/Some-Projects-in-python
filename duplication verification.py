'''
Whenever you compare 2 numbers ina list,dictionnary or any kind of
data structures,you need to set two variables

Same with sorting objects,etc ...

'''

#Verification module
numbers = [3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1 ,len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], "is a duplicated")
            break

#LINEAR RESOLUTION
print("LINEAR RESOLUTION")
num2 = [55456,87,975757,34,987,65546565,98758585,986875754653642]

for i in range(len(num2)): 
    for j in range(i+1,len(num2)): #i must be compared to j
        if num2[i] > num2[j]:
            num2[i] ,num2[j] = num2[j] ,num2[i] 
        print(num2)

#EASIEST RESOLUTION
print(" ")
print("SIMPLIER RESOLUTION")
num3 = [55456,87,975757,34,987,65546565,98758585,986875754653642]
num3.sort()
print(num3)
