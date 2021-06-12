class Car:

	def __init__(self,brand,color,year):
		self.brand = brand
		self.color = color
		self.year = year 


	@classmethod
	def new_car(cls,text):
		brand,color,year = text.split("-")
		return cls(brand,color,year)



# M = 'mercedec-blue-2006'
# B = 'BMW-black-2009'

# mercedec = Car.new_car(M)
# Bmw = Car.new_car(B)

# print(Bmw.color)



#This will hzlp with the printing method 
class Point:
	def __init__(self,x,y):
		self.x = x 
		self.y = y


	def __repr__(self):
		return f'x:{self.x},y:{self.y}'



# j = Point(2,7)
# print(j)

















