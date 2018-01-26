from collections import Counter, namedtuple, defaultdict, OrderedDict, deque
from csv import reader

"""
#Counter
exList = [1, 1, 1, 1, 5, 6, 7, 8, 2, 6, 7, 8, 5, 5, 5]

counts = Counter(exList)
#print(counts)
# Counter({1: 4, 5: 4, 6: 2, 7: 2, 8: 2, 2: 1})
# (key: number of times key appeared). 4 1s in the list

numThrees = counts[3]
#print(numThrees)
# asking for a value that doesn't exist normally returns an error, will return 0 here

counts[1] = 100
#print(counts[1])
#can modify the values


#can reassign or remove a value
counts[5] = 0
#print(counts[5])

del counts[5]
#print(counts)

#will convert into a list as an ordered list, ordered by number of elements
myList = list(counts.elements())
#print(myList)

#returns thex most common
common = counts.most_common(5)
#print(common)

anotherList = [1, 2, 3, 4, 5]

counts2 = Counter(anotherList)

#can also do subtraction. 0 or less than 0 taken out
together = counts+counts2
#print(together)


#some counter functions that weren't covered yesterday

a = Counter(x=1, y=2, z=3)
b = Counter(x=2, y=3, z=4)

#can run operations on counter objects
#print(a+b)
"""

"""
#namedtuple

saleRecord = namedtuple("saleRecord", "shopId saleDate saleAmount totalCustomers")

#can list values with or without name in the call
shop11 = saleRecord(11, "2018-01-25", saleAmount=1000, totalCustomers=125)
shop12 = saleRecord(12, "2018-01-26", 100000, 1)
#print(shop12)

#print(shop12.saleAmount)

#can convert a list into a namedtuple
myList = [13, "2018-01-27", 100, 5]
newShop = saleRecord._make(myList)
#print(newShop)

#._fields returns the names of the fields
#print(newShop._fields)

#to get values, can just turn back into a list
#print(list(newShop))
"""

"""
#defaultdictionary

booksIndex = defaultdict(lambda: "Not Available")

booksIndex["a"] = "Arts"
booksIndex["b"] = "Biography"
booksIndex["a"] = "Computer"

#print(booksIndex)

#if we try to access a value that doesn't exist it will return a default value
#print(booksIndex["z"])

titleIndex = [("a", "Arts"), ("b", "Biography"), ("c", "Computer"),
              ("a", "Army"),("c", "Chemistry"),]
rackIndex = defaultdict(list)

#the tutorial uses id here instead of i, seems like bad practice to me
for i, title in titleIndex:
    rackIndex[i].append(title)

#print(rackIndex.items())

#By passing the named tuple through to a list, we can get a list of titles grouped together by index
"""

"""
#ordered dictionary

dOrder = OrderedDict()
dOrder['a'] = "Alpha"
dOrder['b'] = "Bravo"
dOrder['c'] = "Charlie"
dOrder['d'] = "Delta"
dOrder['e'] = "Echo"

#print(dOrder.keys(), dOrder.items())

listToDict = [(1,"One"),(2,"Two"),(3,"Three"),(4,"Four"),(5,"Five")]
dictFromList = OrderedDict(listToDict)
#print(dictFromList)

studentMarks={}
studentMarks["Saravanan"]=100
studentMarks["Subhash"]=99
studentMarks["Raju"]=78
studentMarks["Arun"]=85
studentMarks["Hasan"]=67

sortByName = sorted(studentMarks.items(), key=lambda t:t[0])

#sort by grade needs -t instead of t. Looks like it tries t sort smallest to largest by default
sortByGrade = OrderedDict(sorted(studentMarks.items(), key=lambda t:-t[1]))
#print(sortByGrade)
"""

#deque -- double ended queue

myDeque = deque([1,2,3,4,5], maxlen = 5)
myDeque.append(6)
#print(myDeque) #deque([2, 3, 4, 5, 6], maxlen=5)

myDeque.appendleft(1)
#print(myDeque) #deque([1, 2, 3, 4, 5], maxlen=5)

#append, extend, pop all work on the right side by defaul
#can call popleft, extendleft, etc

myDeque.extend([6, 7, 8])
#print(myDeque) deque([4, 5, 6, 7, 8], maxlen=5)

myDeque.pop()
#print(myDeque) #deque([4, 5, 6, 7], maxlen=5)


#if a maxlen value isn't set, the deque won't trim to maintain that value

myDeque = deque([1,2,3,4,5])
myDeque.appendleft(0)
#print(myDeque) #deque([0, 1, 2, 3, 4, 5])
