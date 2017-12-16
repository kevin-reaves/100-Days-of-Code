
import itertools as iter

ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine"]
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Chain Function, groups multiple lists into one. Returns generator

#answer = iter.chain(ints, words, chars)

# An interesting thing to note here, if you run the first one the second one
# will return an empty list
#for item in answer:
#    print(item)

#print(list(answer))

# returns 0, zero, a, b
#iter.chain(ints[:1], words[:1], chars[0:2])

#########################################################################

# islice function. works with count to return generator for certain range

#for i in iter.islice(iter.count(), 0 , 101, 5):
#    print(i)


#########################################################################
# compress function

# returns first and last in this case
#binaryFilter = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

#for i in iter.compress(ints, binaryFilter):
#    print(i)

# ifilter, imap -- these two used to be part of itertools. Now filter, map

# If you accidentally type x & 2 instead of x % 2 you'll be very confused
even = [x for x in ints if x % 2 == 0]
#print(even)

# Filter returns the values that fail the criteria. In this case filters even
odd = list(filter(lambda x: x % 2, ints))
#print(odd)

def square(num):
    return num ** 2

#for item in ints:
#    print(square(item))

#for i in map(square, ints):
#    print(i)

for i in map(lambda x: x ** 2, ints):
    print(i)