from collections import Counter

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

