#regular comment

"""
multi
line
comment
"""

#Operators
#print(1+1)
#print(10-9)

#/ is regular division, // is floor division
#print(5/3)
#print(5//3)

# % is the mod operator, remainder after division
#print(7%3)

#exponent
#print(2**3)

#equality check, != inequality
#print(1==1)

#string = "{} can be {}".format("strings", "interpolated")
#string = "{name} wants to eat {food}".format(name="Bob", food="tacos")
#print(string)

#can index strings
#print("This is a string"[0])

#print(len("this is a string"))

#use etc is None instead of == none

#python is truthy, all except a list of values will return True with bool(item)
#those values are 0, "", [], {}, ()

#can change the endline character
#print("Hello world", end="!")

#userInput = input("What's your name? ")

li = [1,2,3,4,5,6]
#li.append(1)
#print(li[0])
#li.pop()

#returns items 1,2
#print(li[1:3])

#prints the list backwards
#print(li[::-1])

#prints 0-n every other index
#print(li[::2])

#can combine slicing to get every other backwards and such

#[:] does deep copy, makes a brand new list instead of just a pointer
#li2 = li[:]
#print(li2)

#can delete items,
# del li[2]

#del allows ranges to be deleted
#del li[3:]
#print(li)

#del and pop work on index, remove searces for the values

#returns the index of the first matching value
#print(li.index(3))

#li + li2, lists aren't modified
#li.extend(li2), li is modified

#in operator checks if a value is in a list
#print(1 in li)

#tuples are immutable, can't be changed once created

#myTup = (1,2,3)
#print(myTup[0])
#myTup[0] = 12, won't work

#can unpack tuples into variables
#a, b, c = (1,2,3)
#print(a,b,c)

#variable swap trick uses tuple unpacking
#a,b = b,a
#print(a,b)

#dictionaries are key/value pairs, hashmaps

#myDict = {"one": 1, "two": 2}
#print(myDict)

#can check keys and values
#print(myDict.keys(), myDict.values())

#myDict["NotThere"], throws an error
#myDict.get("NotThere"), returns None

#myDict.get("NotThere", "default"), can specify a default with get

#del myDict["value"]

#sets are like lists, only contain one of each value

#mySet = {1,1,2,2,3,3,4,4,5,5}
#print(mySet)

#items passed to a set have to be immutable, tupes are supported but not lists

# & intersection
# - difference
# ^ symmetric difference
# >= superset
# <= subset

"""
someVar = 5

if someVar > 10:
    print("bigger than 10")
elif someVar < 10:
    print("smaller than 10")
else:
    print("is 10")

animals = ["dog", "cat", "pony"]
for animal in animals:
    print("{} is a mammal".format(animal))
"""

#for x in range(100):
#    print(x)

#lower, upper, step
#for x in range(0,100,10):
#    print(x)

"""
myList = [1,2,3]

try:
    print(myList[100])
except IndexError as e:
    print(e)
"""

"""
def add(x,y):
    return x + y

print(add(100,-5))
"""

#*args, **kwargs for unknown nums of args

#python has first class functions, can pass a function as an argument or return it
"""
def createMult(x):
    def mult(y):
        return x*y
    return mult

times10 = createMult(10)
print(times10(100))
"""