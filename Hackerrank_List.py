#Objective: perform operations based on user inputs
N = int(input())#keeps track of how many operations must be performed
    my_list = []#list that will be augmented
    for op in range(N):#iterates through all operations
        instruction = input().split(' ')#splits each instruction
        if instruction[0] == "insert":
            my_list.insert(int(instruction[1]), int(instruction[2]))
        elif instruction[0] == "print":
            print(my_list)
        elif instruction[0] == "remove":
            my_list.remove(int(instruction[1]))
        elif instruction[0] == "append":
            my_list.append(int(instruction[1]))
        elif instruction[0] == "sort":
            my_list.sort()
        elif instruction[0] == "pop":
            my_list.pop()
        elif instruction[0] == "reverse":
            my_list.reverse()