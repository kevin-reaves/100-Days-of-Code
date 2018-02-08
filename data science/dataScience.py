import csv
import numpy

#https://www.dataquest.io/blog/numpy-tutorial-python/
#at 1-Dimensional NumPy Arrays

"""
alcoholOverNine = []
with open ("winequality-red.csv") as red:
    wines = list(csv.reader(red, delimiter=";"))
    for x in range(1, len(wines)):
        if float(wines[x][10]) > 9:
            alcoholOverNine.append(wines[x])
with open("alcoholOverNine.csv", "w", newline="") as red:
    writer = csv.writer(red, delimiter=",")
    for line in alcoholOverNine:
        writer.writerow(line)
"""

"""
with open ("winequality-red.csv") as red:
    winesTemp = list(csv.reader(red, delimiter=";"))
    wines = numpy.array(winesTemp[1:], dtype=numpy.float)
    print(wines.shape)
"""

#emptyArray = numpy.zeros((3,4))
#print(emptyArray)

#creates a 3x4 array of random numbers 0-1
#print(numpy.random.rand(3,4))

#skip header allows you to skip without loop
wines = numpy.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
#print(wines)

#grabs index wines[2][6]
#print(wines[2,6])

#supports array slicing
#print(wines[0:3,3])

#prints whole fourth row
#print(wines[:,3])

#wines[1,5] = 10
#print(wines[1,5])

#wines[:10] = 50
#print(wines[:10])

#thirdWine = wines[3,:]
#print(thirdWine)
#print(thirdWine[1])

#(10,10) will print a 10x10 array, (10) will print a 1x10
#print(numpy.random.rand(10))

#multidimensional arrays

"""
yearOne = [
        [500, 505, 490],
        [810, 450, 678],
        [234, 897, 430],
        [560, 1023, 640],
    ]
"""

#print(yearOne)
#print(yearOne[0][0])
#print(yearOne[0])

earnings = [
            [
                [500, 505, 490],
                [810, 450, 678],
                [234, 897, 430],
                [560, 1023, 640]
            ],
            [
                [600, 605, 490],
                [345, 900, 1000],
                [780, 730, 710],
                [670, 540, 324]
            ]
          ]

earnings = numpy.array(earnings)
#print(earnings[0][0][0])
#print(earnings.shape)

# : basically means everything here
#: : 0 returns all of the 0th inside elements
# 500, 810, 234, etc
#print(earnings[:,:,0])


#numpy stores data types in c and maps them to python
#print(wines.dtype)

#astype copies the array and returns a new array with the specified data type
winesInt = wines.astype(int)
#print(winesInt)
#print(winesInt.dtype)

#won't change earnings, will return a new array
#print(earnings[:, :, 0] + 10)
#print(earnings)

# += will change the array in place
#earnings[:, :, 0] += 10
#print(earnings)

#can add arrays together
#print(wines[:, 11] + wines[:, 11])

"""
Broadcasting

Unless the array are the exact same size, numpy will try broadcasting to make
elementwise operators work

last dimension of each array is compared, if len are equal or one is len of 1
keep going

if they aren't equal or =1, error

keep checking until the shortest array is out of dimensions

Compatible because of 3
A: (50,3)
B  (3,)

Compatible because of 2
A: (1,2)
B  (50,2)

Not compatible
A: (50,50)
B: (49,49)
"""

#arrayOne = numpy.array(
#    [
#        [1,2],
#        [3,4]
#        ]
#    )

#arrayTwo = numpy.array([4,5])
#print(arrayOne + arrayTwo)

#sum of every 11th item
#print(wines[:,11].sum())
#axis=0 is the same as wines[0,:,:] + wines[1,:,:], etc
#a good way to make sure the axis worked, call .shape
#the shape should be the same as the number of rows
#print(wines.sum(axis=0))

#there are several others
#mean, std, min, max, etc

#trueFalse = wines[:,11] > 5
#print(trueFalse)

#equalsTen = wines[:,11] == 10
#print(equalsTen)

#print(wines.shape)
wines = wines[1,:].reshape((2,6))
#print(wines.shape)
print(wines)
