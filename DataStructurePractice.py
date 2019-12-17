#The purpose of this program is to create one of each data structure.
#A List, Tuple, and Dictionary will be created. 
#Various method of presentation and augmentation will be applied to these data structures.

listExample = ["Apples","Oranges","Grapes"]
print("'listExample' has a data type of: ",type(listExample))
print("The elements in the list are: ",*listExample,sep=', ')

tupleExample = ("Triangle","Circle","Square")
print("\n"+"'tupleExample' has a data type of: ",type(tupleExample))
print("The elements in the tuple are: ",*tupleExample,sep=', ')

setExample = {"Mountains","Beaches","Cities"}
print("\n"+"'setExample' has a data type of: ",type(setExample))
print("The elements in the set are: ",*setExample,sep=', ')

dictExample = {"Hardware" : "Integrated Circuit", "Software" : "CLion"}
print("\n"+"'dictExample' has a data type of:", type(dictExample)) 
print("The key to value relationships in 'dictExample' are: ")
for x,y in dictExample.items():
	print(x,":",y)

print("\n"+"========================"+"\n")

listFunctions = [" ","Access / Change index elements","Add","Remove","Copy","Join"]
tupleFunctions = [" ","Access","Add","Remove","Copy","Join"]
setFunctions = [" ","Add","Remove","Join"]
dictFunctions = [" ","Access / Change index elements","Remove","Copy","Nest"]

print("Lists are ordered and changable data structures")
print("Functions include:")
for functions in range(1,6):
	print(functions,": ",listFunctions[functions])

listExample.append("Cherry")
print("'listExample' after adding is: ",*listExample,sep=', ')
listExample.pop()
print("'listExample' after removing is: ",*listExample,sep=', ')
newListExample = listExample.copy()
LastListExample = listExample + newListExample
print("'listExample' after joining is:")
print(*LastListExample,sep=', ')

print("\n"+"========================"+"\n")

print("Tuples are ordered but unchangeable data structures")
print("Functions include:")
for functions in range (1,6):
	print(functions,": ",tupleFunctions[functions])
print("Methods used to perform these operations are the same as in a list")

print("\n"+"========================"+"\n")

print("Sets are unordered and unchangeable data structures")
print("Functions include:")
for functions in range(1,4):
	print(functions,": ",setFunctions[functions])
setExample.add("Vacations")
print("The new 'setExample' after adding is: ",*setExample,sep=', ')
setExample.remove("Vacations")
print("The new 'setExample' after removing is: ",*setExample,sep=', ')
newSetExample = {"Work","Study"}
newSetExample.update(setExample)
print("'setExample' after joining is: ",*newSetExample,sep=', ')

print("\n"+"========================"+"\n")

print("Dictionaries are unordered and changeable data structures")
print("Functions include:")
for functions in range(1,5):
	print(functions,": ",dictFunctions[functions])
dictExample["Software"] = "IntelliJ"
print("'dictExample' after changing a value is: ")
for x,y in dictExample.items():
	print(x,":",y)
dictExample["Algorithm"] = "Recursion"
print("'dictExample' after adding is: ")
for x,y in dictExample.items():
	print(x,":",y)
dictExample.pop("Algorithm")
print("'dictExample' after removing is:")
for x,y in dictExample.items():
	print(x,":",y)
dictExpanded = {"Design":"Top Level", "CLock":"Slow"}
dictExample["Components"] = dictExpanded
print("'dictExample' after nesting a dictionary:")
for x,y in dictExample.items():
	print(x,":",y)
