#Create a list. Add numbers. Create an array of strings. Overwrite the 
#list with the strings
print("Input a number representing the size of a list:")

size = int(input())
FinalList = [] 
print("The data type of 'FinalList' is:")
print(type(FinalList))

for values in range(size):
	FinalList.append(values)
print("\n"+"The values in the list are:")
print(*FinalList,sep=', ')

FunArray = ["I2C","UART","SPI","Threading"]

for values in range(len(FinalList)):
	FinalList[values] = FunArray[values]

print("\n"+"The new values in the list are:")
print(*FinalList,sep=', ')
