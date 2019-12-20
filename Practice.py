iterate = int(input())
Student = []
Names = []

for items in range(iterate):
	name = input()
	grade = float(input())
	student =[name,grade]
	Student.append(student)

Student.sort(key = lambda x: x[1])
lowest = Student[0][1]
for people in Student:
	if people[1] == lowest:
		Student.remove(people)

secondLowest = Student[0][1]
for people in Student:
	if people[1] == secondLowest:
		Names.append(people[0])

Names.sort()
for people in Names:
	print(people)