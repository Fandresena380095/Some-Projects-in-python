'''
#simple help key = value

tick2 = {}

i = int(input("total length :"))

for x in range (0,i) :
    inDict = input("key : ")
    outDict = input("value : ")
    tick2[inDict] = outDict
    x += 1
print(tick2)

'''
'''
Here you have a age processing payment:
    Those who are under 18 pay 5
    Those above pay 20

Now you wanna set a new age limit x(which is the input)
    1-The goal of your algorithm is to calculate the benefit % if you
        change the limit age by x
    2-You will have x as an input and a percentage as an output
    3-Remember:
    AB : Actuall benefit
    XB : Benefit with x as imput

    TotalB(in %) = ((XB -AB)/AB)*100
    
'''

tick = {
    "Dave" : 23 ,
    "John" : 20 ,
    "Durk" : 26 ,
    "Dako" : 29 ,
    "Jill" : 20 ,
    "Jeanette" : 17 ,
    "Jane" : 15 ,
    "Julia" : 29 ,
    "Jake" : 12 ,
    "Jakob" : 15 ,
    "Jason" : 15 ,
    "Jared" : 25 ,
    }


#1-GET THE TOTAL BENEFITS FROM THE DICTIONARY 
totalBA = 0 
for i in tick: 
    if tick[i] >= 18:
        totalBA += 20
    else :
        totalBA += 5

#2-DEFINE A NEW AGE LIMIT AND IT'S BENEFIT
totalBX = 0
x = int(input("Changed age limit : "))
for a in tick:
    if tick[a] >= x:
        totalBX += 20
    else :
        totalBX += 5

#3-CALCULATE THE PERCENTAGE OF THE BENEFIT WITH THE NEW AGE LIMIT
percentageBX = ((totalBX-totalBA)/totalBA)*100
print(int(percentageBX))

#4-PRINT THE NUMBER OF AULTS AND TEENAGERES (FACULTATIF)
adults = {k:v for k,v in tick.items() if v>=18}
print("Nombres de personnes excedant 18 ans :" ,len(adults))
teenagers = {k:v for k,v in tick.items() if v<18}
print("Nombre de personnes en dessous de 18 ans :", len(teenagers))



























    
    


    
    
    

