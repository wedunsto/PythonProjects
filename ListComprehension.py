print("Enter 4 numbers:")#prompt the user to enter numbers 
print("the first three numbers will serve as x,y, and z coordinates.")
print("the last number will serve as the threshold for those coordinates.")
x = int(input())#store the x coordinate threshold value
y = int(input())#store the y coordinate threshold value
z = int(input())#store the z coordinate threshold value
n = int(input())#store the n conditional value

for xaxis in range(x+1):#from 0 to max x value
	for yaxis in range(y+1):#from 0 to max x value
		for zaxis in range(z+1):#from 0 to max x value
			if xaxis+yaxis+zaxis != n:#if the conditional is satisfied
				print([xaxis, yaxis, zaxis])#print coordinates

#print[
#    [i,j,k]
#    for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n
#]
