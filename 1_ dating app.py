class Male:

    keys = []
    values = []
    basic_info = {}
    common_passions = set()

    

    def __init__(self, name = None,age = None, city = None ,job = None) :
        self.name = input("Your name :")
        self.keys.append(self.name)
        self.basic_info['Name'] = self.name
        self.age = int(input("Your age :"))
        self.keys.append(self.name)
        self.basic_info['Age'] = self.age
        self.city = input("Your city :")
        self.keys.append(self.name)
        self.basic_info['City'] = self.city
        self.job = input("Current job :")
        self.keys.append(self.name)
        self.basic_info['Job'] = self.job
        print("Okey",self.name,",you are",self.age,"Years old ,you live in",self.city,",and you are a",self.job,"right? \n Are you sure you sure your informations are valid ?")
        self.confirmation = (input("Yes/No :"))
        self.conf_l = self.confirmation.lower()
        if  'yes' in self.conf_l  :
            if self.age < 18 :
                print("Well ,you are not old enough ,bye")
                return
            print("Your informations have been registered. \n Do you wanna tell more about yourself ?")
            choice = input("yes/later :")
            if "yes" in choice :
                self.more_about()
            else:
                print("Ok ,see ya later")
                print("You can always use the .more_about() method to call us")
                return 
        else :
            print("Okey let's redo it")
            self.basic_info = {}
            self.keys = [] 
            Male.__init__(self, name = None,age = None, city = None ,job = None)
            

    def more_about(self):
        print("So ,tell about your passions ")
        print("What would be a perfect first date ?")
        self.activity1 = input("cinema/restaurant/McDo/shopping/bar/home :")
        self.common_passions.add(self.activity1)
        print("Do you have an artistic side ?")
        self.activity2 = input("dance/music/drawing/painting/singing/writting :")
        self.common_passions.add(self.activity2)
        print("It's a friday night... How would you like to spend it ?")
        self.activity3 = input("home/bar/cinema/club/gaming/working :")
        self.common_passions.add(self.activity3)
        print("It is dinner time and you want to impress your loved one,what do you cook ?")
        self.activity4 = input("I don't know ?/speciality/MrDelivery/simple stuff :")
        self.common_passions.add(self.activity4)
        print("Time to choose a junk food ?")
        self.activity5 = input("burger/pizza/tacos/fries/chips/sandwitch/nope :")
        self.common_passions.add(self.activity5)
        print("Favourite car brand ?")
        self.activity6 = input("BMW/mercedes/audi -chevrolet/dodge/triumph -japanese.... :")
        self.common_passions.add(self.activity6)
        print("Your house is on fire ,what do you save first ?")
        self.activity7 = input("books/computer/people/pets... :")
        self.common_passions.add(self.activity7)
        print("Ok it's family time. You .... it  ?")
        self.activity8 = input("hate/love :")
        self.common_passions.add(self.activity8)
        print("Are you a people person ?")
        self.activity9 = input("yes/occasionally/nope :")
        self.common_passions.add(self.activity9)
        print("Best vacation ?")
        self.activity10 = input("home/beach/hikking/mountain/forest/adventure :")
        self.common_passions.add(self.activity10)
        print("If you were to choose a playlist ?")
        self.activity11 = input("pop/jazz/rock/metal/reggae/rnb/blues/hip-hop :")
        self.common_passions.add(self.activity11)
        print("Do you believe in God ?")
        self.activity12 = input("yes/nope :")
        self.common_passions.add(self.activity12)
        print("What is your biggest fear ?")
        self.activity13 = input("ghost/death/loosing/phobia/star wars :")
        self.common_passions.add(self.activity13)
        print("Say you have the chance to resurrect a dead person,who would you choose ?")
        self.activity14 = input("relative/Michael Jackson/Beethoven/Iron Man :")
        self.common_passions.add(self.activity14)
        print("What is your biggest weakness ?")
        self.activity15 = input("fear/superiority complex/food/lust/laziness :")
        self.common_passions.add(self.activity15)
        print("What do you think of opposite sex's friendship ?")
        self.activity16 = input("exists/doesn't exist/friendzone :")
        self.common_passions.add(self.activity16)
        print("You are the only person left on Earth ,what do you do first ?")
        self.activity17 = input("eat/travel/sleep/panic/explore/go crazy :")
        self.common_passions.add(self.activity17)
        print("What do you think of politics ?")
        self.activity18 = input("Bullshit/good/manipulative/stop it :")
        self.common_passions.add(self.activity18)
        print("Okey almost done \n How would you see yourself in 7 years ?")
        self.activity19 = input("engineer/teacher/billionaire/homeless/in prison/ok you must stop these stupid questions :")
        self.common_passions.add(self.activity19)
        print("Finally ,do you believe in true love ?")
        self.activity20 = input("yes/no :")
        self.common_passions.add(self.activity20)

class Female:

    keys = []
    values = []
    basic_info = {}
    common_passions = set()

    

    def __init__(self, name = None,age = None, city = None ,job = None) :
        self.name = input("Your name :")
        self.keys.append(self.name)
        self.basic_info['Name'] = self.name
        self.age = int(input("Your age :"))
        self.keys.append(self.name)
        self.basic_info['Age'] = self.age
        self.city = input("Your city :")
        self.keys.append(self.name)
        self.basic_info['City'] = self.city
        self.job = input("Current job :")
        self.keys.append(self.name)
        self.basic_info['Job'] = self.job
        print("Okey",self.name,",you are",self.age,"Years old ,you live in",self.city,",and you are a",self.job,"right? \n Are you sure you sure your informations are valid ?")
        self.confirmation = (input("Yes/No :"))
        self.conf_l = self.confirmation.lower()
        if 'yes' in self.conf_l :
            if self.age < 18 :
                print("Well ,you are not old enough ,bye")
                return
            print("Your informations have been registered. \n Do you wanna tell more about yourself ?")
            choice = input("yes/later :")
            if  "yes" in choice :
                self.more_about()
            else:
                print("Ok ,see ya later")
                print("You can always use the .more_about() method to call us")
                return 
        else :
            print("Okey let's redo it")
            self.basic_info = {}
            self.keys = []
            Male.__init__(self, name = None,age = None, city = None ,job = None)
            

    def more_about(self):
        print("So ,tell about your passions ")
        print("What would be a perfect first date ?")
        self.activity1 = input("cinema/restaurant/McDo/shopping/bar/home :")
        self.common_passions.add(self.activity1)
        print("Do you have an artistic side ?")
        self.activity2 = input("dance/music/drawing/painting/singing/writting :")
        self.common_passions.add(self.activity2)
        print("It's a friday night... How would you like to spend it ?")
        self.activity3 = input("home/bar/cinema/club/gaming/working :")
        self.common_passions.add(self.activity3)
        print("It is dinner time and you want to impress your loved one,what do you cook ?")
        self.activity4 = input("I don't know ?/speciality/MrDelivery/simple stuff :")
        self.common_passions.add(self.activity4)
        print("Time to choose a junk food ?")
        self.activity5 = input("burger/pizza/tacos/fries/chips/sandwitch/nope :")
        self.common_passions.add(self.activity5)
        print("Favourite car brand ?")
        self.activity6 = input("BMW/mercedes/audi -chevrolet/dodge/triumph -japanese.... :")
        self.common_passions.add(self.activity6)
        print("Your house is on fire ,what do you save first ?")
        self.activity7 = input("books/computer/people/pets... :")
        self.common_passions.add(self.activity7)
        print("Ok it's family time. You .... it  ?")
        self.activity8 = input("hate/love :")
        self.common_passions.add(self.activity8)
        print("Are you a people person ?")
        self.activity9 = input("yes/occasionally/nope :")
        self.common_passions.add(self.activity9)
        print("Best vacation ?")
        self.activity10 = input("home/beach/hikking/mountain/forest/adventure :")
        self.common_passions.add(self.activity10)
        print("If you were to choose a playlist ?")
        self.activity11 = input("pop/jazz/rock/metal/reggae/rnb/blues/hip-hop :")
        self.common_passions.add(self.activity11)
        print("Do you believe in God ?")
        self.activity12 = input("yes/nope :")
        self.common_passions.add(self.activity12)
        print("What is your biggest fear ?")
        self.activity13 = input("ghost/death/loosing/phobia/star wars :")
        self.common_passions.add(self.activity13)
        print("Say you have the chance to resurrect a dead person,who would you choose ?")
        self.activity14 = input("relative/Michael Jackson/Beethoven/Iron Man :")
        self.common_passions.add(self.activity14)
        print("What is your biggest weakness ?")
        self.activity15 = input("fear/superiority complex/food/lust/laziness :")
        self.common_passions.add(self.activity15)
        print("What do you think of opposite sex's friendship ?")
        self.activity16 = input("exists/doesn't exist/friendzone :")
        self.common_passions.add(self.activity16)
        print("You are the only person left on Earth ,what do you do first ?")
        self.activity17 = input("eat/travel/sleep/panic/explore/go crazy :")
        self.common_passions.add(self.activity17)
        print("What do you think of politics ?")
        self.activity18 = input("Bullshit/good/manipulative/stop it :")
        self.common_passions.add(self.activity18)
        print("Okey almost done \n How would you see yourself in 7 years ?")
        self.activity19 = input("engineer/teacher/billionaire/homeless/in prison/ok you must stop these stupid questions :")
        self.common_passions.add(self.activity19)
        print("Finally ,do you believe in true love ?")
        self.activity20 = input("yes/no :")
        self.common_passions.add(self.activity20)
        



def Match(x,y):
    if isinstance(x,Male) and isinstance(y,Female):
        try :
            c = x.common_passions & y.common_passions
            if len(c) >= 18 :
                print("You both are made for one another")
                return
            elif len(c) < 18 and len(c) >= 15:
                print("It's a match")
                return
            elif len(c) < 15 and len(c) >= 10 :
                print("There is a way ,nothing is impossible")
                return
            elif len(c) < 10 and len(c) >= 5:
                print("Ok ,maybe you should try with someone else")
                return
            else :
                print("Ok ,you guys are like water and fire ,dead on")
                return
        except :
            print("We will find a match for you ")

Zack = Male()
July = Female()

Match(Zack ,July)
        


























    
        
                       
    
    
