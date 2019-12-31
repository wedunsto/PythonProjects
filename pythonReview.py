#The objective of this python script, is to display a review of current python knowledge
#Class:
class Review:#Creates a class in python


	def __init__(self,name, age):#Creates a function with args, initializes classes properties
		self.name = name
		self.age = age
		print("I am "+name+" I am "+age+" years old.")

	def Traveling(self):#Creates a no args function
		place = "Washington"
		destinations = ("California","Washington","Pennsylvania","North Carolina","South Carolina")
		if place in destinations:#Creates a branching statement
			print("I have visited "+place)
		else:
			print("I have not visited "+place)

	def Car(self,year,color,make,model):#Creates a function with args
		print("My car is a "+year+" "+color+" "+make+" "+model)

	def Hobbies(self):
		funStuff = ["Programming","Sitting outside","Listening to music","Going to concerts"]
		for objectives in funStuff:#Creates a looping statement
			print(objectives)


testReview = Review("William","27")
testReview.Traveling()
print("I enjoy: ")
testReview.Hobbies()
