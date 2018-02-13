x = 27
y = 12

# shifts
#110011 -> 11001100. Moved the original set of numbers up by 2
#print(x<<2)

#11011 -> 110. Moves down by 2, drops numbers that get shifted too far
#print(x>>2)


#bitwise and
#11011
#01100
######
#01000
#print(x & y)

#bitwise or - if both are 0, output 0. else output 1
#11011
#01100
######
#11111
#print(x | y)

#bitwise complement -> -(x+1). 2's complement
#print(~x)

#bitwise xor - num ^ itself = 0

#print(x^x)