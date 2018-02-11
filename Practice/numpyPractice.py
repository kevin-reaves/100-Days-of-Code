import numpy as np

#numpy is faster than standard lists
#a = np.array([[1,2,3,4],[4,5,6,7]])
#print(a)
#prints the number of dimensions
#print(a.ndim)
#datatypes
#print(a.dtype)
#print(a.size)
#print(a.shape)

#must be able to logically move into the row/column given
#a = a.reshape(4,2)
#print(a)

#print(a[0,2] also works here. Doesn't work in standard lists
#print(a[0,2])

#prints the third index of all rows. passing 1 only returns third of first row
#print(a[0:,3])

#returns third item on rows 0-2
#print(a[0:2, 3])
#testList = [[1,2,3,4,5],[6,7,8,9,10]]
#print(testList[0,2])

#will print 5 values that are equally spaced between 1 and 3
#a = np.linspace(1,3,5)
#print(a)

# = np.arange(1,10000, 1)
#for item in a:
#    print(item)

#print(a.max())
#print(a.min())
#print(a.sum())
#print(a.std())
#prints sqrt for each element in array
#print(np.sqrt(a))

# [[1,2,3,4]
#  [4,5,6,7]]

# returns 5, 7, 9, 11. 1+4, 4+7, etc
#print(a.sum(axis=0))

#a = np.array([[1,2,3,4],[4,5,6,7]])
#b = np.array([[11,12,13,14],[14,15,16,17]])

#numpy +_ will do matrix addition on the two arrays
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

#to actually concat two arrays, either horizontal or vertical stacking

#print(np.vstack((a,b)))
#print(np.hstack((a,b)))

# e^item
#a = np.array([1,2,3,4,5,6])
#print(np.exp(a))

#natural log of item, can use log10 for log base 10
#print(np.log(a))


