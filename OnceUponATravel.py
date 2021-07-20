# This is not an optimal way to do this kind of content
print("Hello there! So nice to have you !")
name = input("So what is your name ?: ")
print("Hmmm",name,"....what a beautiful name")
age = int(input("So ,how old are you ?: "))

if age >= 18 :
    print("Ok ,you are old enough ")
    yes_or_no = input("Do you wanna start the game ? (yes/no) :").lower()
    if yes_or_no == "yes":
        print("Okey! Let's strart the adventure.")   
        print('''
             One day, after a very long week ,you decided to go on a road trip
             to the countryside. You were at an intersection, and you had to 
             choose between left and right. 
              Which way do you choose ? 
              ''') 
        way1 = input("(left/right) :")
        if way1 == "left":
            print("""
                    So, after driving for 3 hours, you arrived at a lake. The air is fresh,
                   the sky is blue, everything looks pretty.
                   You are now free to do whatever you wanna do.
                   Would you rahter keep it safe and rest, or go swim ? 
                  """)
            deci = input("(rest/swim) :")
            if deci == 'swim':
                print("You took of your shirt , and you are ready to dive in !!.")
                print("""
                      But you can't decide where to swim .... take a risk by swimming in deep water
                      or keep it safe and playing in shallow water
                      """)
                print("Where do you go")
                ds = input("(deep/shallow) :")
                if ds == "shallow":
                    print('''
                          So now you are pretty tired after playing for 2 hours in the shallow waters.
                          Now it's time to go back home .But now your car didn't start and there is literally 
                          no one else around. It is 6PM and you decided to walk by your own.
                          At 8PM , you came into an intersection where you saw an old house.
                          Would you rather rest in the house or carry on ?
                          ''')
                    hc = input("(house/road) :")
                    if hc == 'house':
                        print('''
                              So you knocked and knocked and knocked.
                              Eventually someone came to open.
                              But the last thing you saw was a gun pointing at you and now you are travelling
                              with St Peter to the garden of Eden. Nice game, bad choice
                              ''')
                    else : 
                        print('''
                              So yeah ,you walked for 2 hours now. Youare exchausted and starving.
                              Now there is a car that stopped right behind you .
                              The lady inside the car looked so nice.
                              Are you going to accept the ride ?
                              ''')
                        yn = input("(yes/no) :")
                        if yn == 'yes':
                            print('''
                                    So you entered in .The lady was actually a college girl.
                                    She had dark eyes with chocolate colored hair and was kinda cute.
                                    You guys had a very nice conversation ... You told her your adventure ...
                                    She laughed all the way throughout the trip .
                                    Then eventually you looked at each other's eyes deeply ,you kissed...
                                    From there on ,things got serious ,you married the girl.
                                      
                                    Now you are 30 years old, has 2 beautiful children ,and from time to time , still
                                    tell them how you guys met.
                                           END.
                                    ''')
                        else : 
                            print('''
                                  So unsure, you decided to walk and say no to the lady. 
                                  But she really insisted and a voice inside of you said "YES DIVE IN"
                                                                      So you entered in .The lady was actually a college girl.
                                    She had dark eyes with chocolate colored hair and was kinda cute.
                                    You guys had a very nice conversation ... You told her your adventure ...
                                    She laughed all the way throughout the trip .
                                    Then eventually you looked at each other's eyes deeply ,you kissed...
                                    From there on ,things got serious ,you married the girl.
                                      
                                    Now you are 30 years old, has 2 beautiful children ,and from time to time , still
                                    tell them how you guys met.
                                           END.
                                  ''')
                        
                    
                else :
                    print("""
                          So you actually jumped right in.
                          But in the middle of the river, a hole absorbed you and you died.
                          You are now in heaven waiting for your last judgement.
                                                   END
                          """)
                    
                
            else :
                print("So you felt asleep for 10 hours, you have been robbed")
                print("""
                      Your bag is empty, your tant is gone, your car has been stolen
                      you loose !
                      """)
            
            
            
        elif way1 == "right" : 
            print('''
                  So you went to the right, and your car crashed in a river.
                  Now you are stuck in the middle of nowhere and cry for help
                  
                                           END.
                  ''')












    else:
        print("OK bye then !")
else : 
    print("Hey !You are underage..... byeeeee")
