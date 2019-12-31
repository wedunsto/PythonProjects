#Objective: Complete objectives in Mom's homework#3 assignment
class William:#Creates the William class
	def __init__(self,name, city):#defines the default constructor for William class
		self.name = name#sets the name property to the user entered name
		self.city = city#sets the city property to the user entered city
		print("Hi, my name is "+name+" and I am from "+city)#dynamically prints out statement

	def Favorite_places(self,place1,place2,place3):#defines the function
		places = [place1,place2,place3]#creates a list of the favorite places
		print("My favorite cities are: ")
		for locations in places:#iterates through places list
			print(locations)#prints strings in the places list

	def Favorite_foods(self,food):
		foods = ("Slow cooked Beef","Fried Chicken","Sushi")#creats a set of food items
		if food in foods:#checks if food is an item in the foods set
			print(food+" is one of my favorite foods")
		else:#if food is not in foods
			print(food+" is not one of my favorite foods")

#test = William("William","Warminster")
#test.Favorite_places("Nagano","Amsterdam","Ontario")
#test.Favorite_foods("Papaya")
#test.Favorite_foods("Sushi")

