#The objective of this Class is to solve quadratic equations
import math

class Quadratic_Equation:#Creates the quadratic equation class
	a = 0#initializes the class attribute a to 0
	b = 0#initializes the class attribute b to 0
	c = 0#initializes the class attribute c to 0
	minusFactor = 0#initializes the class attribute minusFactor to 0
	positiveFactor = 0#initializes the class attribute positiveFactor to 0

	def __init__(self,coefficent1,coefficient2,coefficient3):
	#defines the init funcn and takes in the quadratic coefficents
		self.a = coefficent1#sets the object attribute a to first coefficient
		self.b = coefficient2#sets the object attribute b to second coefficient
		self.c = coefficient3#sets the object attribute c to third coefficient
		print("The quadratic equation is: "+str(self.a)+"x^2 + "+str(self.b)+"x + "+str(self.c))

	def Factor(self):#defines the factor function to solve the quatic equation
		subSR = math.pow(self.b,2)-4*self.a*self.c#calcuates the math under square root
		squareRoot = math.sqrt(subSR)#calculates the square root of subSR
		self.minusFactor = (-self.b - squareRoot)/(2*self.a)#finds the minus of the equation
		self.positiveFactor = (-self.b + squareRoot)/(2*self.a)#finds the positive of the equation

		print("The solution is x = "+str(self.minusFactor)+", "+str(self.positiveFactor))
		#outputs the solution

#Test = Quadratic_Equation(6,11,-35)
#Test = Quadratic_Equation(1,3,-4)
#Test.Factor()
