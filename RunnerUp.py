#The objective is to print the second highest number in a list
Scores = [-7,-7,-7,-7,-6] 
print("The original scores are:")
print(*Scores,sep=' ')
Scores.sort()
print("The sorted scores are:")
print(*Scores,sep=' ')

TempList = []

for score in Scores:
	if score < Scores[-1]:
		TempList.append(score)
print("The values in 'TempList' are:")
print(*TempList,sep=' ')
print("The second highest score is:")
print(TempList[-1])
