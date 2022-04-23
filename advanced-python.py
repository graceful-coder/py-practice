# The purpose of this file is to take notes
# On how to write more efficient and readable (i.e. elegant) code

from email.policy import default
import itertools
import collections
from enum import Enum
import logging

# How to use the All() fn
# Exercise: Detect Boolean false items in a list

list1 = [2, 3, 6, 0, 5, 5]

print(all(list1)) #returns True if 0 exists in the list

# The Any() fn returns False if any item in the list evaluates to false

# Use the min, max, and sum functions on items in a list

print("Min should be 0: ", min(list1))
print("Min should be 6: ", max(list1))
print("Sum should be 21: ", sum(list1))

# Using filters
# Detect if a number in a list is odd

def isOdd(x):
    if x % 2 == 0:
        return False
    else:
        return True

# ///////////////////////////////
# Let's use the filter fn to elegantly remove even numbers from the list
odds = list(filter(isOdd, list1))
print(odds)


#Elegantly use Iterators in Python

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
daysFr = ['Dim', 'Lundi', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

# i = iter(days)
# print(next(i))
# print(next(i))
# print(next(i))

#Gracefully reading in a file

with open('testfile.txt', 'r') as filepointer:
    for line in iter(filepointer.readline, ''): #Passes a filepointer and sentinel null value to read until EoF
        print(line)

# for j in days:
#     print(j)

# for k in daysFr:
#     print

# Instead of:
for l in range(len(days)):
    print('Day ', l+1, days[l])

# Use Enumerate
for l,m in enumerate(days, start=1):
    print('Daylhlhjk ',l, m)

# Zip fn combines collections!

for m in zip(days, daysFr):
    print(m)

# Enhance with enumerate

for i,m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], ' = ', m[1], ' in French')


# Show only the lower case letters
chars = "alsjkfdOISHGJkasjflkj"

def removeUpperCase(x):
    if x.isupper():
        return False
    else:
        return True

lowers = list(filter(removeUpperCase, chars))
print(lowers)

# Use map to take a sequence of numbers and create a new sequence of their squares

def square(x):
 
    return x**2

squares = list(map(square, list1))

# ALERT! THIS MAP CAN BE REWRITTEN AS A COMPREHENSION:
# squares = [ x**2 for x in list1]

for i, m in enumerate(zip(list1, squares)):
    print(m[0], ' -> ', m[1], ' after squaring')
print(square.__doc__)

grades = [66, 73, 93, 85, 90, 77]

# Convert the grades to letter grades

def toLetter(x):
    if x >= 90:
        return "A"
    elif x >= 80 and x < 90:
        return "B"
    elif x >= 70 and x < 80:
        return "C"
    elif x >= 65 and x < 70:
        return "D"
    else:
        return "F"

lettergrades = list(map(toLetter, grades))
print(lettergrades)

# INFINITE ITERATORS

# Cycle back to the beginning of a sequence after iterating to the end

seq = ['Joe', 'John', 'Mike']
cycle1 = itertools.cycle(seq)
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

# Count to 100 in increments of 10

count = itertools.count(100, 10)
print(next(count))
print(next(count))
print(next(count))

# Aggregate all the numbers in the sequence

seq2 = [10, 30, 20, 40, 50]

acc = itertools.accumulate(seq2)

print(list(acc))


# Chain two sequences together

x = itertools.chain(seq, seq2)

print(list(x))

# SUPER GRACEFUL
# How to pass in a variable number of arguments to a fn

def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

seq1 = [1,2,3]
seq2 = [5,10,15]
print(addition(*seq1))
print(addition(*seq2))

# Namedtuples for creating more graceful, readable code

Point = collections.namedtuple("Point", "x y")

p1 = Point(10, 40)
p2 = Point(20, 30)

print(p1.x, p2.y)


# How to use a Dictionary in Python
# Use a dictionary to count each element in a list

fruits = ['apple', 'pear', 'orange', 'pear', 'banana', 'apple', 'pear',
'banana', 'banana']

fruitCounterDictionary = {} # This instantiates a dictionary type object

# Loop over the list and update a counter of repeating fruits in the list

for fruit in fruits:
    if fruit in fruitCounterDictionary.keys():
        fruitCounterDictionary[fruit] += 1
    else:
        fruitCounterDictionary[fruit] = 1 # Instantiates the count = 1 as the base case

# Print the dictionary key value pairs in a readable format

# for (key,value) in fruitCounterDictionary.items():
#     print(key + ':' + str(value))


# Use a default dict object from Collections 
# In place of a dictionary to make the code more readable

fruits2 = ['apple', 'pear', 'orange', 'pear', 'banana', 'apple', 'pear',
'banana', 'banana']

fruitCounterDefaultDict = collections.defaultdict(int) # The default dict constructs the dictionary WITH an initial fruit count value of 0

# fruitCounterDefaultDict = collections.defaultdict(lamda: 100) constructs the dictionary WITH an initial fruit count value of 100

# Now... the dictionary doesn't have to initialize the fruit count value 

for fruit in fruits2:
        fruitCounterDefaultDict[fruit] += 1
    
for (key,value) in fruitCounterDefaultDict.items():
    print(key + ':' + str(value))


# Using Counters (Remember: Counters are dictionaries with key/value pairs)

names1 = ['Bob', 'Becky', 'Chad', 'Darcy', 'Frank', 'Hannah', 'Kevin',
 'James', 'James', 'Melanie', 'Penny', 'Steve']

names2 = ['Bill', 'Barry', 'Cindy', 'Debbie', 'Frank', 'Gabby', 'Kelly', 'James', 'Joe', 'Sam', 'Tara', 'Ziggy']

# Create a Counter for names1 and names2

c1 = collections.Counter(names1)
c2 = collections.Counter(names2)

# How many students in names1 are named James?

print(c1["James"], ' instances of James in names1') # Prints count for key = "James"

# How many students in names2?

print(sum(c1.values()), ' students in names1')

# Combine names1 and names2
c1.update(c2)
print(sum(c1.values()), ' students in names1')

# What are the three most common names in both classes?

print(c1.most_common(3))

# Separate the names lists again

c1.subtract(names2)

# Now

print(c1.most_common(3))

# What names are common between the two classes?

print(c1 & c2)

# ENUMERATIONS

class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4

def enumsPractice():
    
    # enums have human readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))
    print(repr(1))

    # enums have a name and a value property
    # * SO READABLE! :D *
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])

enumsPractice()

# if __name__ == "__main__":
#     main()

# Practice creating classes

class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

# Create a new Person object
cls1 = Person()

# Print their first name and age
print(cls1.fname + ' is ' + str(cls1.age))


# COMPREHENSIONS

evens = [2, 4, 6, 8, 10]
odds = [1, 3, 4, 7, 9]

# BEFORE

evenSquared = list(map(lambda x: x**2, filter( lambda x: x > 4 and x < 16, evens)))
print(evenSquared)

# AFTER using Comprehension

evenSquared2 = [y**2 for y in evens]
print(evenSquared2)

oddsSquared = [x**2 for x in odds if x > 3 and x < 17]
print(oddsSquared)

# BEFORE convert Celsius to Fahrenheit

celsTemps = [0, 12, 34, 100]

# AFTER this comprehension, the dict creates key value pairs

tempDict = {t: t*9/5 + 32 for t in celsTemps if t < 100}
print(tempDict[12])

# BEFORE two sport names with names and their jersey numbers - Merge into one team

team1 = {'Jones': 24, 'Jameson': 18, 'Smith': 5, 'Burns': 7}
team2 = {'White': 12, 'Macke': 88, 'Perce': 4}

# This is as complex as a comprehension should get: two expressions
newTeam = {k:v for team in (team1, team2) for k,v in team.items()}
print(newTeam)

# Comprehensions in sets

ctemps = [5, 10, 12, 14, 10, 23, 41,30, 12, 24, 12, 18, 29]

# Build a set of unique Fahrenheit temperatures

ftemps1 = [(t*9/5)+32 for t in ctemps]
ftemps2 = {(t*9/5)+32 for t in ctemps}

print(ftemps1 , " This is a list with duplicate values")
print(ftemps2 , " This is a SET with only unique values")


# 2nd example: Build a set from an input source

sTemp = "The quick brown fox jumped over the lazy dog"

# Turn all chars to upper case in a set of unique chars and omit spaces
chars = {c.upper() for c in sTemp if not c.isspace()}
print(chars)