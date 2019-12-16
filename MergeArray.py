#create a list that contains the even elements from the first array
#and the odd elements from the second array
EvenArray = ["Football", "Basketball", "Baseball", "Soccer"]#Create first array
OddArray = ["Skateboard", "Snowboard", "Ski", "BMX"]#Create second array
print("The even array consists of:")
for americansports in EvenArray:
	print(americansports)
print("\n"+"The odd array consists of:")
for altsports in OddArray:
	print(altsports)
JoinList = list()#Create empty list
for x in range(len(EvenArray)):#Fill indexes
	JoinList.append("")
for x in range(len(EvenArray)):#add even elements to proper indexes
	if x%2 == 0:
		JoinList[x] = EvenArray[x]
for x in range(len(OddArray)):#add odd elements to proper indexes
	if x%2 != 0:
		JoinList[x] = OddArray[x]
print("\n"+"All the values in the merged list are:")
for x in JoinList:
	print(x)
