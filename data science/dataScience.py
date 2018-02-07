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
