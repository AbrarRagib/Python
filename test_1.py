# a = 5
# b = 7
# c= a+b

# # print (c)
# a = input("Give a number: ")
# b = input("Give a number: ")
# sum = int(a) + int(b)

# print("Sum:", sum)



# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)

#GLobal Variable
# x = "awesome"
# Y = "Dump"

# def myfunc():
#   print("Python is "+Y)

# myfunc()

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

#User Input Sum
# a = input("Int:")
# b = input("Float:")
# c = input("Complex:")
# Sum = int(a)+ float(b)+complex(c)
# print("Sum is:", Sum)







"""
print(1)
print(2)
Comments, Escape Sequences & Print Statement 
"""

# print("Apple\nOrange")#New Line
# print('Hello, \"WhatsUp?\"') #Escape Sequence

# print("Pi=",3.,1,4,1,6, sep="~", end="Arkisu mone nai\n") # sep= Separator, end = specify what should be end.
# print('Done')

#Variable and Data Type
# a=1
# print(a)

# Ragib=9
# b=Ragib
# print(b)

# a = 1
# b = True
# c = "Ragib"
# d = None
# print("a=",a, "\nb=",b, "\nc=",c, "\nd=",d)
# print("Type of a is:", type(a))
# print("Type of b is:", type(b))
# print("Type of c is:", type(c))
# print("Type of d is:", type(d))
# print("Type of a is",type(a),"type of b is:",type(c))


#4 Build in data Types 

# 1. List, **Can be change Mutable,List items are ordered, changeable, and allow duplicate values.List items are indexed, the first item has index [0], the second item has index [1] etc.


# 2. Tuples, ** Not changeable Immutable, Tuple items are ordered, unchangeable, and allow duplicate values.Tuple items are indexed, the first item has index [0], the second item has index [1] etc.


# 3. Sets, **A set is a collection which is unordered, unchangeable*, and unindexed.Set items are unordered, unchangeable, and do not allow duplicate values.


# 4. Dictionaries, **Dictionary items are ordered, changeable, and do not allow duplicates.


# list1=[1,2,3,[-2,-3],["Apple"]]
# print(list1)

# tuple1 = (("Tiger","Lion"),("RAT"))
# print(tuple1)

# set1 = {"apple", "banana", "cherry"}
# print(set1)

# Dict1 = {"Ragib":"WHO","Vote":True}
# print(Dict1)


#Operators
# print(26//5) #Floor division
# print(5%3) #Modulus
# print(2**3) #Exponential

# a=50
# b=50
# print("Addition a+b:",a+b)
# print("Addition a-b:",a-b)
# print("Addition a*b:",a*b)
# print("Addition a/b:",a/b)




# #IF condition 
# a = 100
# b = 200

# if a > b:
#     print("a is greater than b")

# elif a < b:
#     print("b is grater than a")

# elif a == b:
#     print("Equal")

# elif a != b:
#     print("Not equal")


# else:
#     print("error")



#Typecasting (2 types)
# 1. Explicit
# 2. Implicit

# a = "1"
# b = "2"
# print(int(a)+int(b))#Explicit 

# a = 1
# b = 4.5
# print(a+b)#Implicit


#User Input:

# a = input("Who is the Don? ")
# print("The don is : Mr.",a)

# x = input("Enter First number:")
# y = input("Enter Second number:")
# print(x+y)
# print(int(x) + int(y))


#String
# name = 'Ragib'
# quotes = '''He said, "Nothing is impossible"'''
# test = 'What "is" up?'
# test2 = "What is \"up\" next?"


# print(quotes)
# print(test)
# print(test2)
# print(name[0])
# print(name[1])

# print("Lets use a for loop\n")
# for character in name:
#     print(character)


#Strings Slicing and operations [String are immutable]

# names = "Abrar,Ragib"
# print(names[0:6])

# fruit =  "Mangoo"
# mangoLen = len(fruit)
# print(mangoLen)
# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:4])
# print(fruit[0:])
# print(fruit[:])
# print(fruit[:])

# nm = "haRry"
# print(nm[-4:-2])

# count= "Bangladesh"
# print(count[4:7]) #Here Bangladesh is [0,1,2,3,4,5,6,7,8,9]
#                    #4 means l/3 & 7 means 6/d. (x normal,y always -1)




# count= "Bangladesh"
# print(count[-2:])


# a= "!!!Ragib !!!!!! Ragib!!"
# print("Lenth:",len(a))
# print("My String:",a)
# print("In Upper Case:",a.upper())
# print("In Upper Case:",a.lower())
# print("Striped:",a.rstrip("!")) #Only for tail
# print(a.replace("Ragib","Abrar"))
# print(a.split(" "))
# b = "my Blog Heading"
# print(b.capitalize())

# c = "Whats Up?"
# print(len(c))
# print(len(c.center(50)))

# print("Ragib count:",a.count("Ragib"))
# print(c.endswith("?"))#Boolean datatype
# c = "Whats Up?"
#     #012345678 
# print(c.endswith("Up",6,8))

# d = "What is you name?"## Find index number
# print(d.find("is"))
# print(d.index("iss")) #Through error and programme should be run.


# str1 = "WelcomeToTheConsole1"
# print(str1.isalnum())
# str1 = "Welcome"
# print(str1.isalpha())

# str1 = "hello world"
# print(str1.islower())


# str1 = "We wish you a Merry Christmas!"
# #str1 = "        \n"#False given
# print(str1.isprintable())

# str1 = "        "       #using Spacebar
# print(str1.isspace())
# str2 = "        "       #using Tab
# print(str2.isspace())

# str1 = "World Health Organization" 
# print(str1.istitle())

# str1 = "WORLD HEALTH ORGANIZATION" 
# print(str1.isupper())

# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# str1 = "Python Is a Interpreted Language" 
# print(str1.swapcase())

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.title())








# If Else Statements

# Conditional operators 
# >, <, >=, <=, ==, !=




# a = int(input("Enter your age: "))
# print("Your age is: ",a)

# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("You can drive")
#     print("Why this line is printed?")
# else:
#     print("Yo can not drive!")
# print("WHy")



# num = int(input("Enter integer valuer of a num: "))

# if (num < 0):
#     print("Your number is negative")
# elif (num == 0):
#     print("Your number is Zero")
# else:
#     print("Your number is positive")



# num = int(input("Enter Your Number: "))
# if (num < 0):
#     print("Your number is Negative!")
# elif (num > 0):
#     if(num <= 10):
#         print("Number is between 1-10")
#     elif(num > 10 and num <= 20):
#         print("Number is between 10-20")
#     else:
#         print("Number is grater than 20")
# else:
#     print("Number is Zero")



# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime



# import time

# # Get the current hour
# current_hour = time.localtime().tm_hour #This retrieves the current hour (0-23) from the system's local time.

# # Determine the appropriate greeting
# if 5 <= current_hour < 12:
#     greeting = "Good Morning!"
# elif 12 <= current_hour < 18:
#     greeting = "Good Afternoon!"
# else:
#     greeting = "Good Evening!"

# Print the greeting
# # print(greeting)
# import time
# current_hour  = time.localtime().tm_hour
# if 5 <= current_hour < 12:
#     print("Good morning")
# elif 12 <= current_hour < 18:
#     print("Good afternoon")
# else:
#     print("Good Evening")

# for k in range(1, 5001):
#     print(k)



#Match Case Statement/ Switch Case:



# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)

# x = int(input("Enter the value of X: "))
# match x:
#     case 0:
#         print("X is Zero")
#     case 4:
#         print("Case is 4")
#     case _ if x!=90:
#         print(x,"X is not 90")
#     case _ if x!=80:
#         print(x,"X is not 80")
#     case _:
#         print(x)








#For Loops:


# money = ["dollar","pound","real"]
# for i in money:
#     print(i)
#     if i == "pound":
#         break
    


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x) 


# colors = ["Red", "Green", "Blue"]

# for color in colors:
#     print(color)
#     for char in color:
#         print(char)

# for x in range(5):
#     print(x+1)

# for x in range(1,5):
#     print(x)

# for x in range(1, 10, 5): #Step Range()
#     print(x)


#While Loop:


# i = 0
# while(i<=5):
#     print(i)
#     i = i + 1
# print("Done with the loop")

# i = int(input("Give the value of i: "))
# while(i<=50):
#     i = int(input("Give the value of i: "))
#     print(i)
# print("Done with while loop")


# count = 5
# while(count >= 0):
#     print(count)
#     count = count - 1
# else:
#     print("Done")



#Emulate do while loop

# do {
  # loop body;
# }while(condition);

#Break and Continue:

# for i in range(12):
#     if(i == 10):
#       break
#     print("5 X", i+1,"=", 5 * (i+1))
# print("Stop the loop")

# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i%100 == 0):
#     break






#Functions:

# def isGreater(a,b):
#     if (a>b):
#         print("First Number is grater than Second Number")
#     else:
#         print("Second number is grater or Equal")


# a = 6
# b = 1
# isGreater(a,b)

# def Average(a, b, c):
#     print("The average of three number is: ", (a+b+c)/3)

# Average(9,10,11)


# def average(*numbers):
#   # print(type(numbers))
#   sum = 0
#   for i in numbers:
#     sum = sum + i
#   # print("Average is: ", sum / len(numbers))
#   # return 7
#   return sum / len(numbers)


# # average(4, 6)
# # average(b=9)

# c = average(5, 6, 7, 1)
# print(c)




#List: 
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.


    
# marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)

 

#marks = [3, 5, 6, "Ragib", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0]) 
# print(marks[1]) 
# print(marks[2]) 
# print(marks[3]) 
# print(marks[4]) 

# print(marks[-3]) #Negative index 
# print(marks[len(marks)-3]) #Positive index
# print(marks[5-3])
# print(marks[2])

# if 7 in marks:
#     print("Yes")
# else:
#     print("No")


# if "Ragib" in marks:
#     print("Yes")
# else:
#     print("No")

# if "gib" in "Ragib": #FInd specific strings from string
#     print("Yes")
# else:
#     print("No")

# print(marks)
# print(marks[:])
# print(marks[1:-1])
# print(marks[1:4])

# print(marks)
# print(marks[1:8])
# print(marks[1:8:2]) #Jump Index: 2 means jump 2 index 



#List comprehension 

# lst = [i for i in range(5)]
# print(lst)

# lst = [i*i for i in range(5)]
# print(lst)

# lst = [i*i for i in range(5) if i%2 == 0]
# print(lst)







#List Methods:

# l = [1, 2, 3, 4, 5, 6]
# print(l)
# l.append(7)
# print(l)

# l = [4, 5, 3, 2, 1, 5]
# print(l)
#l.sort()
# l.sort(reverse= True)
# l.reverse()
# print(l.index(3))
# print(l.count(5))
# m = l.copy()
# m[0] = 0
# print(l)
# print(m)

# l.insert(1, 899)
# print(l)

# m = [300, 400, 500, 50000]
# l.extend(m) #extend list but l will be change
# print(l)


#Concatenating two list:
# m = [300, 400, 500, 50000]
# k = m + l 
# print(k)













#Tuples in Python: Tuples are not Changeable!!!

# tup = (1, 3, 9, 20, "Ragib", True)
# #tup = (1)#Python will be confused if you don not add any comma in tuples!!!


# print(type(tup), tup)
# print(tup[0])
# print("Length is: ",len(tup))
# print(tup[-1])

# if "Ag" in "Ragib":
#     print("Yes")
# else:
#     print("False")

# tup2 = tup[1:4]
# print(tup2)


# countries = ("USA", "Russia", "France", "Canada")
# countries2 = ("Bangladesh", "Nepal", "Bhutan")

# merge = countries + countries2
# print(merge)

# tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# # res = tuple1.count(3)
# # res = tuple1.index(3)
# # res = tuple1.index(311)
# # res = tuple1.index(3, 4, 8)
# res = len(tuple1)
# print('Count of 3 in tuple1 is:', res)









#f-strings
# letter = "My name is {1} and I am from {0}"
# country = "Bangladesh" 
# name = "Ragib"
# print(letter.format(country,name))

# print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)
# # print(txt.format())
# print(type(f"{2 * 30}"))







#Doc strings in Python and PEP8




# def square(n):
#   '''Takes in a number n, returns the square of n''' #Must be written last below square!!!  
#   print(n**2)
# square(5)
# print(square.__doc__)


# def sum(n):
#   '''Takes two int number n, returns sum value of n'''
#   print(n+n)
# sum(5)
# print(sum.__doc__)

#PEP 8 >> python>> import this 
#The Zen of Python, by Tim Peters




#Recursion in python


# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(4))




# def fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

# # Number of terms you want in the Fibonacci series
# num_terms = 10

# # Generate and print the Fibonacci series
# fib_series = fibonacci(num_terms)
# print(fib_series)


# def fibonacci_recursive(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fib_seq = fibonacci_recursive(n - 1)
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#         return fib_seq

# # Number of terms you want in the Fibonacci series
# num_terms = 10

# # Generate and print the Fibonacci series
# fib_series = fibonacci_recursive(num_terms)
# print(fib_series)












#Sets in python:  duplicate value shows one, no order maintain

# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

# a = {"ragib", 34, 4, 5, 2, True, 4}
# print(a)

# ragib = {}
# print(type(ragib))

# for value in a:
#     print(value)



# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# print(cities)


# II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)


# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)



# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

# Example:


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)



# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))















# #Dictionaries in Python (In past dic are unordered)  
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.




# dic = {
#     "Ragib": "Human being",
#     "Spoon": "Object"
# }

# print(dic["Ragib"])

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)



# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

# # Example:
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible'))



# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

# # Example:
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.values())


# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.keys())


# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info.items())


# info = {'name':'Karan', 'age':19, 'eligible':True}
# # print(info) 
# # print(info.keys())
# # print(info.values())

# # for key in info.keys():
# #   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 


#Git push



# git add .
# git commit -m "Your commit message"
# git push origin main

















# # Dictionary Methods in Python
# Dictionary uses several built-in methods for manipulation.They are listed below


# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)
# info.update({'age':20})
# info.update({'DOB':2001})
# print(info)


# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.

# clear():
# The clear() method removes all the items from the list.

# # Example:
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)



# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.pop('eligible')
# print(info)



# popitem():
# The popitem() method removes the last key-value pair from the dictionary.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# info.popitem()
# print(info)



# del:
# we can also use the del keyword to remove a dictionary item.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# print(info)
# del info['age']
# print(info)


# If key is not provided, then the del keyword will delete the dictionary entirely.

# Example:

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# print(info)
# del info
# print(info)









# for Loop with else in Python
# Python - else in Loop
# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.


# Example:


# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")


# i = 0
# while i<7:
#   print(i)
#   i = i + 1
#   # if i == 4:
#   #   break

# else:
#   print("Sorry no i")

# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")







# Exception Handling
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.
# Exceptions in Python
# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.


# Python try...except
# try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

# Syntax:
# try:
#      #statements which could generate 
#      #exception
# except:
#      #Soloution of generated exception

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")




# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")