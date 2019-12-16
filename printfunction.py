#The idea is to print N consecutive numbers on the same line
n = int(input())
print(*range(1,n+1),sep='')
