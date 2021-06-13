import random


print("Guess a number between 1 and 10")    
number = random.randint(0,10)
carryOn = True
guess_number = 0

def narrow_down(g):
    x = random.randint(0,g)
    y = random.randint(0,g)
    
    opening_range = number - x
    closing_range = number + y
    
    print("The number is between",opening_range,"and",closing_range)

    
starting_narrow_down = 4

while carryOn :
    
    guess_number += 1
    print("Guess number,try "+ str(guess_number))
    guess = int(input("Guess the number :" ))
    starting_narrow_down -= 1

    if guess == number :
        print("well done")
        carryOn = False

    elif guess_number >=3 :
        print("Oups ,you loose")
        carryOn = False

    else :
        if guess > 11 or guess < 1 :
            print("Not the good range,try again")
        else :
            print("Try again")
        narrow_down(starting_narrow_down)
        
        
        
    
    
        
    
        
    
