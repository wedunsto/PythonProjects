#Objective: print the student name(s) with the second lowest scores
    Students=[]#Holds all the student names and scores
    Names=[]#Holds all the student names above the lowest score
    Result=[]#Holds the student names with the second lowest score

    for _ in range(int(input())):#stores the names and scores
        name = input()
        score = float(input())
        Students.append([name,score])

    Students.sort(key = lambda x: x[1])#sorts the nested list by scores
    
    for people in Students:#stores the student names and scores above the lowest score
        if people[1] > Students[0][1]:
            Names.append(people)

    for people in Students:#stores the student names with the second lowest score
        if people[1] == Names[0][1]:
            Result.append(people[0])

    Result.sort()#sorts the results alphabetically
    
    for people in Result:#prints out the names 
        print(people)