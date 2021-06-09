#coffee machine methods
class CoffeeMachine :
    import time
    water_container = 0
    water_temp = 10
    coffee_container = 0
    coffee_liquid = 0

    def __init__(self ,color ,brewtime = 120): 
        self.color = color
        self.brewtime = brewtime
        print(" Water/Coffee ratio is important ")
        print(" For 1000mL of water, try between 60(weak) and 79(strong) grams of coffee ")
        print(" For 500mL of water, try between 28(weak) and 39(strong) grams of coffee ")
        self.water_container = int(input('Please ,add some water :'))
        self.coffee_container = int(input("Please ,add some coffee :"))


    def make_coffee(self):
        self.__verify()

    def add_water(self ):
        quantity = int(input('Water added :'))
        self.water_container = self.water_container + quantity

    def add_coffee(self ):
        quantity = int(input('Coffee added :'))
        self.coffee_container = self.coffee_container + quantity

    def __verify(self):
        while self.water_container == 0 or self.coffee_container == 0:
            if self.water_container == 0 and self.coffee_container == 0:
                print("Please add some water and coffee")
                self.add_water()
                self.add_coffee()
            elif self.coffee_container == 0:
                print("Please add some coffee into the filter")
                self.add_coffee()
            elif self.water_container == 0:
                print("Please add some water")
                self.add_water()
        else :
            if self.__is_not_overflowing() == True:
                self.__verify_quantity()                
                

    def __is_not_overflowing(self):
        while self.water_container > 1000:
            print(f"Your quantity :{self.water_container}, Quantity needed : 1000")
            print("The water container is full")
            print("Please remove some water")
            water_removed = int(input("Quantity you remove :"))
            self.water_container = self.water_container - water_removed
        return True

    def __verify_quantity(self):
        ratio = self.water_container / self.coffee_container
        while ratio > 18 or ratio < 12.5:
            print("////____Your water/coffee ratio isn't optimal____////")
            print(f"Water quantity :{self.water_container} ,Coffee quantity :{self.coffee_container}")
            print("Your ratio :",ratio)
            print("Normal ratio : 12.5 < r < 18 ")
            if ratio > 18 :
                print("Your coffee is going to be very weak")
                print("Try to use less water or more coffee")
                water_added = int(input("Water quantity added :"))
                self.water_container = self.water_container + water_added
                coffee_added = int(input("Coffee quantity added :"))
                self.coffee_container = self.coffee_container + coffee_added
                ratio = self.water_container / self.coffee_container
            elif ratio < 12.5 :
                print("Your coffee is going to be very strong")
                print("Try to use more water or less coffee")
                water_added = int(input("Water quantity added :"))
                self.water_container = self.water_container + water_added
                coffee_added = int(input("Coffee quantity added :"))
                self.coffee_container = self.coffee_container + coffee_added
                ratio = self.water_container / self.coffee_container
            if self.water_container != True:
                self.__is_not_overflowing()
                
        self.__brew()

    def __brew(self) :
        import time
        print("Boiling the water ")
        self.__boil_water()
        print("Brewing the coffee")
        print("Please wait...")
        time.sleep(5)
        self.coffee_liquid += 1
        self.__alert()
        self.water_container = 0
        self.coffee_container = 0

    def __boil_water(self):
        import time
        print("Please wait... ")
        time.sleep(5)
        self.water_temp = 100
        print("Your water is boiled ")

    def __alert(self):
        print("Your coffee is ready ")
        print('E - N - J - O - Y - ! - ! - !')
        print('')
        print('  )   )    )    )   )')
        print(' (   (    (    (   (')
        print(' )   )    )    )   )')
        print('(   (    (    (   ( ')
        print('-------------------')
        print('\                 /--|')
        print(' ( \               /   |')
        print('  \             /----|')
        print('   \           /')
        print('--------------------')
        
        
        
        
        
            


java = CoffeeMachine("red")

java.make_coffee()
        

