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














# Finally Clause
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:

# try:
#    #statements which could generate 
#    #exception
# except:
#    #solution of generated exception
# finally:
#     #block of code which is going to 
#     #execute in any situation


#     The finally block is executed irrespective of the outcome of try……except…..else blocks
# One of the important use cases of finally block is in a function which returns a value.

# Example:
# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")






# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)















# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.



# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")


# Defining Custom Exceptions
# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Here's the syntax to define custom exceptions:

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...

# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

# a = int(input("Enter any value between 5 and 9: "))

# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")





# questions = [
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")









# If ... Else in One Line
# There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:

# a = 2
# b = 330
# print("A") if a > b else print("B")
# You can also have multiple else statements on the same line:

# Example
# One line if else statement, with 3 conditions:

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")
# Another Example
# result = value_if_true if condition else value_if_false
# This syntax is equivalent to the following if-else statement:

# if condition:
#     result = value_if_true
# else:
#     result = value_if_false
# Conclusion
# The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
# However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.




# a = 330000
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B")

# c = 9 if a>b else 0
# print(c)













# Enumerate function in python
# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# # Loop over a list and print the index and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
# The output of this code will be:

# 0 apple
# 1 banana
# 2 mango
# As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

# Changing the start index
# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:

# # Loop over a list and print the index (starting at 1) and value of each element
# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits, start=1):
#     print(index, fruit)
# This will output:

# 1 apple
# 2 banana
# 3 mango
# The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:

# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(f'{index+1}: {fruit}')
# This will output:

# 1: apple
# 2: banana
# 3: mango
# In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:

# # Loop over a tuple and print the index and value of each element
# colors = ('red', 'green', 'blue')
# for index, color in enumerate(colors):
#     print(index, color)
# And here's an example with a string:

# # Loop over a string and print the index and value of each character
# s = 'hello'
# for index, c in enumerate(s):
#     print(index, c)








# marks = [12, 56, 32, 98, 12,  45, 1, 4]

# # index = 0
# # for mark in marks:
# #   print(mark)
# #   if(index == 3):
# #     print("Harry, awesome!")
# #   index +=1

# for index, mark in enumerate(marks, start=1):
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")




# Virtual Environment
# A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

# To create a virtual environment in Python, you can use the venv module that comes with Python. Here's an example of how to create a virtual environment and activate it:

# # Create a virtual environment
# python -m venv myenv
# # Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate
# # Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat
# Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

# To deactivate the virtual environment, you can use the deactivate command:

# # Deactivate the virtual environment
# deactivate
# The "requirements.txt" file
# In addition to creating and activating a virtual environment, it can be useful to create a requirements.txt file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

# To create a requirements.txt file, you can use the pip freeze command, which outputs a list of installed packages and their versions. For example:

# # Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt
# To install the packages listed in the requirements.txt file, you can use the pip install command with the -r flag:

# # Install the packages listed in the requirements.txt file
# pip install -r requirements.txt
# Using a virtual environment and a requirements.txt file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.







# How importing in python works
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

# import math
# Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

# import math
# result = math.sqrt(9)
# print(result)  # Output: 3.0
# from keyword
# You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:

# from math import sqrt
# result = sqrt(9)
# print(result)  # Output: 3.0
# You can also import multiple functions or variables at once by separating them with a comma:

# from math import sqrt, pi
# result = sqrt(9)
# print(result)  # Output: 3.0
# print(pi)  # Output: 3.141592653589793
# importing everything
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.

# from math import *
# result = sqrt(9)
# print(result)  # Output: 3.0
# print(pi)  # Output: 3.141592653589793
# Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

# The "as" keyword
# import math as m
# result = m.sqrt(9)
# print(result)  # Output: 3.0
# print(m.pi)  # Output: 3.141592653589793
# The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.

# import math
# print(dir(math))
# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

# In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.




# from math import sqrt, pi
# from math import pi, sqrt as s
# import math as math_builtin_python

# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0

# from harry import welcome, harry
# import harry as hr
# import math

# print(dir(math))
# print(math.nan, type(math.nan))
# hr.welcome()
# print(hr.harry)



















# if "__name__ == "__main__" in Python
# The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

# In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

# Here's an example of how the if __name__ == __main__ idiom can be used:

# def main():
#     # Code to be run when the script is run directly
#     print("Running script directly")
# if __name__ == "__main__":
#     main()
# In this example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom checks whether the __name__ variable is equal to __main__. If it is, the main function is called.

# Why is it useful?
# This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script:

# def main():
#     print("Running script directly")
# if __name__ == "__main__":
#     main()
# If you run this script directly, it will output "Running script directly". However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:

# import script
# script.main()  # Output: "Running script directly"
# This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.

# Is it a necessity?
# It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script. You can still run a script without it by simply calling the functions or running the code you want to execute directly. However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.

# In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.



# import Demo_1

# Demo_1.welcome()

























# os Module in Python
# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

# Here are some common tasks you can perform with the os module:

# Reading and writing files The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:

# import os
# # Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)
# # Read the contents of the file
# contents = os.read(f, 1024)
# # Close the file
# os.close(f)
# To open a file for writing, you can use the os.O_WRONLY flag:

# import os
# # Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)
# # Write to the file
# os.write(f, b"Hello, world!")
# # Close the file
# os.close(f)
# Interacting with the file system
# The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory:

# import os
# # Get a list of the files in the current directory
# files = os.listdir(".")
# print(files)  # Output: ['myfile.txt', 'otherfile.txt']
# You can also use the os.mkdir function to create a new directory:

# import os
# # Create a new directory
# os.mkdir("newdir")
# Running system commands
# Finally, the os module provides functions for running system commands. For example, you can use the os.system function to run a command and get the output:

# import os
# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# You can also use the os.popen function to run a command and get the output as a file-like object:

# import os
# # Run the "ls" command and get the output as a file-like object
# f = os.popen("ls")
# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# # Close the file-like object
# f.close()
# In summary, the os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.




# import os
 

# for i in range(0, 100):
#     os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
    


# import os 
# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))





# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")

# Do not run the code, it will create too much folders












# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
























# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))








# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
  
















#   local and global variables
# Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

# A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =. For example:

# x = 5
# y = "Hello, World!"
# Now, let's talk about local and global variables.

# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

# Here's an example to help clarify the difference:

# x = 10 # global variable
# def my_function():
#   y = 5 # local variable
#   print(y)
# my_function()
# print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
# In this example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function.

# The global keyword
# Now, what if we want to modify a global variable from within a function? This is where the global keyword comes in.

# The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. Here's an example:

# x = 10 # global variable
# def my_function():
#   global x
#   x = 5 # this will change the value of the global variable x
#   y = 5 # local variable
# my_function()
# print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
# In this example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

# It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

# I hope this tutorial has helped clarify the differences between local and global variables and how to use the global keyword in Python. Thank you for watching!
  










# x = 10000  # global variable


# def my_function():
#   global x
#   x = 5  # this will change the value of the global variable x
#   y = 5  # local variable


# my_function()
# print(x)  # prints 5
# # print(y) # this will cause an error because y is a local variable and is not accessible outside of the function



# Opening a File
# Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# Here's an example of how to open a file for reading:

# f = open('myfile.txt', 'r')
# By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.


# Modes in file
# There are various modes in which we can open files.

# 1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# 2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# 3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# 4. create (x): This mode creates a file and gives an error if the file already exists.

# 5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# 6. binary (b): used to handle binary files (images, pdfs, etc).




# Reading from a File
# Once we have a file object, we can use various methods to read from the file.

# The read() method reads the entire contents of the file and returns it as a string.

# f = open('myfile.txt', 'r')
# contents = f.read()
# print(contents)




# Writing to a File
# To write to a file, we first need to open it in write mode.

# f = open('myfile.txt', 'w')
# We can then use the write() method to write to the file.

# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')










# Closing a File
# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

# To close a file, you can use the close() method.

# f = open('myfile.txt', 'r')
# # ... do something with the file
# f.close()
# The 'with' statement
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

# with open('myfile.txt', 'r') as f:
#     # ... do something with the file


# reading a file
# f = open('text.txt','r')
# text = f.read()
# print(text)
# f.close()



# writing a file
# f = open('text.txt','w')
# f.write('hello, world!')
# f.close()


# # auto open and close when using with
# with open('text.txt', 'a') as f:
#   f.write("Hey I am inside with")














# readlines() method
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# The readlines() method reads all the lines of the file and returns them as a list of strings.

# writelines() method
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

# Here's an example of how to use the writelines() method:

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()
# This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()
# It is also a good practice to close the file after you are done with it.





# f = open('text.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

# f = open('text.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()










# seek() and tell() functions
# In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in io module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes, and in-memory buffers.

# seek() function
# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

# with open('file.txt', 'r') as f:
#   # Move to the 10th byte in the file
#   f.seek(10)
#   # Read the next 5 bytes
#   data = f.read(5)
# tell() function
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For example:

# with open('file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#   # Save the current position
#   current_position = f.tell()
#   # Seek to the saved position
#   f.seek(current_position)
# truncate() function
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

# Here is an example of how to use the truncate function:

# with open('sample.txt', 'w') as f:
#   f.write('Hello World!')
#   f.truncate(5)
# with open('sample.txt', 'r') as f:
#   print(f.read())


# with open('text.txt', 'w') as f:
#   f.write('Hello World3!')
#   f.truncate(3)

# with open('text.txt', 'r') as f:
#   print(f.read())










# Lambda Functions in Python
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

# lambda arguments: expression
# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example of how to use a lambda function:

# # Function to double the input
# def double(x):
#   return x * 2
# # Lambda function to double the input
# lambda x: x * 2
# The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.

# Lambda functions can have multiple arguments, just like regular functions. Here is an example of a lambda function with multiple arguments:

# # Function to calculate the product of two numbers
# def multiply(x, y):
#     return x * y
# # Lambda function to calculate the product of two numbers
# lambda x, y: x * y
# Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

# # Lambda function to calculate the product of two numbers,
# # with additional print statement
# lambda x, y: print(f'{x} * {y} = {x * y}')
# In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

# Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look into later.




# def double(x):
#   return x*2

# def appl(fx, value):
#   return 6 + fx(value)

# double = lambda x: x * 2
# cube = lambda x: x * x * x
# avg = lambda x, y, z: (x + y + z) / 3

# print(double(5))
# print(cube(5))
# print(avg(3, 5, 10))
# print(appl(lambda x: x * x , 2))


























# Map, Filter and Reduce
# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# map
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

# map(function, iterable)
# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the map function:

# # List of numbers
# numbers = [1, 2, 3, 4, 5]
# # Double each number using the map function
# doubled = map(lambda x: x * 2, numbers)
# # Print the doubled numbers
# print(list(doubled))
# In the above example, the lambda function lambda x: x * 2 is used to double each element in the numbers list. The map function applies the lambda function to each element in the list and returns a new list containing the doubled numbers.

# filter
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

# filter(predicate, iterable)
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the filter function:

# # List of numbers
# numbers = [1, 2, 3, 4, 5]
# # Get only the even numbers using the filter function
# evens = filter(lambda x: x % 2 == 0, numbers)
# # Print the even numbers
# print(list(evens))
# In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers list and return only the even numbers. The filter function applies the lambda function to each element in the list and returns a new list containing only the even numbers.

# reduce
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

# reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

# Here is an example of how to use the reduce function:

# from functools import reduce
# # List of numbers
# numbers = [1, 2, 3, 4, 5]
# # Calculate the sum of the numbers using the reduce function
# sum = reduce(lambda x, y: x + y, numbers)
# # Print the sum
# print(sum)
# In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3), and so on. The final result is the sum of all the elements in the list, which is 15.

# It is important to note that the reduce function requires the functools module to be imported in order to use it.


























# 'is' vs '==' in Python
# In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

# For example:

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)  # True
# print(a is b)  # False
# In this case, a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.

# One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:

# a = "hello"
# b = "hello"
# print(a == b)  # True
# print(a is b)  # True
# a = 5
# b = 5
# print(a == b)  # True
# print(a is b)  # True
# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

# For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.

# I hope this helps clarify the difference between is and == in Python!



# a = None
# b = None

# print(a is b) # exact location of object in memory
# print(a is None) # exact location of object in memory
# print(a == b) # value


# a = [1,2,3]   # immutable so python create it only once
# b = [1,2,3]

# print(a is b) # exact location of object in memory
# print(a == b) # value

# a = 3  # immutable so python create it only once
# b = 3

# print(a is b) # exact location of object in memory
# print(a == b) # value


# Snake Water Gun
















# Introduction to Object-oriented programming
# Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that are used to write program or code.

# 1). Procedural Programming
# 2). Object-Oriented Programming
# The procedure we are following till now is the “Procedural Programming” approach. So, in this session, we will learn about Object Oriented Programming (OOP). The basic idea of object-oriented programming (OOP) in Python is to use classes and objects to represent real-world concepts and entities.

# A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have. Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform.

# An object is an instance of a class, and it contains its own data and methods. For example, you could create a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance of the Person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.

# One of the key features of OOP in Python is encapsulation, which means that the internal state of an object is hidden and can only be accessed or modified through the object's methods. This helps to protect the object's data and prevent it from being modified in unexpected ways.

# Another key feature of OOP in Python is inheritance, which allows new classes to be created that inherit the properties and methods of an existing class. This allows for code reuse and makes it easy to create new classes that have similar functionality to existing classes.

# Polymorphism is also supported in Python, which means that objects of different classes can be treated as if they were objects of a common class. This allows for greater flexibility in code and makes it easier to write code that can work with multiple types of objects.

# In summary, OOP in Python allows developers to model real-world concepts and entities using classes and objects, encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.

















# Python Class and Objects
# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Creating a Class:
# Let us now create a class using the class keyword.

# class Details:
#     name = "Rohan"
#     age = 20
# Creating an Object:
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.

# Example:
# obj1 = Details()
# Now we can print values:

# Example:
# class Details:
#     name = "Rohan"
#     age = 20
# obj1 = Details()
# print(obj1.name)
# print(obj1.age)








# self parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It must be provided as the extra parameter inside the method definition.

# Example:
# class Details:
#     name = "Rohan"
#     age = 20
#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")
# obj1 = Details()
# obj1.desc()















# Constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# Syntax of Python Constructor
# def __init__(self):
# 	# initializations
# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.

# Types of Constructors in Python
# Parameterized Constructor
# Default Constructor
# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it is known as parameterized constructor.

# These arguments can be used inside the class to assign the values to the data members.

# Example:
# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group
# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")
# Output:
# Crab belongs to the Crustaceans group.
# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.

# Example:
# class Details:
#   def __init__(self):
#     print("animal Crab belongs to Crustaceans group")
# obj1=Details()
# Output:
# animal Crab belongs to Crustaceans group





# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Ragib", "Developer")
# b = Person("Devh", "HR") 
# a.info()
# b.info()
# # print(a.name)
# # a.name = "Divya"
# # a.occ = "HR"
# # a.info()

















# Python Decorators
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

# @decorator_function
# def my_function():
#     pass
# The @decorator_function notation is just a shorthand for the following code:

# def my_function():
#     pass
# my_function = decorator_function(my_function)
# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

# Practical use case
# One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
#     return a + b
# In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.

# Conclusion
# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.





# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello world")

# @greet
# def add(a, b):
#   print(a+b)
  
# # greet(hello)()
# hello()
# # greet(add)(1, 2)
# add(1, 2)























# Getters
# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a simple class with a getter method:

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#     @property
#     def value(self):
#         return self._value
# In this example, the MyClass class has a single property, _value, which is initialized in the init method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property.

# To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute:

# >>> obj = MyClass(10)
# >>> obj.value
# 10
# Setters
# It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter

# Here is an example of a class with both getter and setter:

# class MyClass:
#     def __init__(self, value):
#         self._value = value
#     @property
#     def value(self):
#         return self._value
#     @value.setter
#     def value(self, new_value):
#         self._value = new_value
# We can use setter method like this:

# >>> obj = MyClass(10)
# >>> obj.value = 20
# >>> obj.value
# 20
# In conclusion, getters are a convenient way to access the values of an object's properties, while keeping the internal representation of the property hidden. This can be useful for encapsulation and data validation.









# class MyClass:
#   def __init__(self, value):
#       self._value = value
    
#   def show(self):
#     print(f"Value is {self._value}")
    
#   @property
#   def ten_value(self):
#       return 10* self._value
    
#   @ten_value.setter
#   def ten_value(self, new_value):
#       self._value = new_value/10

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()



# # How would you reverse a string in Python?
# def reverse_string(s):
#     return s[::-1]

# # Example usage:
# print(reverse_string("hello"))  # Output: "olleh"


# String Slicing:

# s[::-1] is a Python string slicing technique used to reverse a string. Here's what it means:
# s[start:stop:step] is the general format for slicing.
# start: The starting index of the slice (optional, defaults to 0).
# stop: The stopping index of the slice (optional, defaults to the end of the string).
# step: This controls how the slice progresses. If it's positive, it slices forward, but if it's negative, it slices backward.
# [::-1] means "start at the end of the string and move backward by one step at a time," effectively reversing the string.


# # Write a function to check if a given string is a palindrome.``
# def is_palindrome(s):
#     # Convert to lowercase and remove spaces
#     s = s.replace(" ", "").lower()
#     # Compare string with its reverse
#     return s == s[::-1]

# # Example usage:
# print(is_palindrome("A man a plan a canal Panama"))  # Output: True
# print(is_palindrome("hello"))  # Output: False



















# Inheritance in python
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Python Inheritance Syntax
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class
# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

# Types of inheritance:
# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance
# We will see the explaination and example of each type of inheritance in the later tutorials







# Single Inheritance:
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.

# Example:
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
 
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
 
# object = Child()
# object.func1()
# object.func2()
# Output:
# This function is in parent class.
# This function is in child class.
# Multiple Inheritance:
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class.

# Example:
# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 
 
# class Father:
#     fathername = ""
 
#     def father(self):
#         print(self.fathername)
 
 
# class Son(Mother, Father):
#     def parents(self):
#         print("Father name is :", self.fathername)
#         print("Mother :", self.mothername)
# s1 = Son()
# s1.fathername = "Mommy"
# s1.mothername = "Daddy"
# s1.parents()
# Output:
# Father name is : Mommy
# Mother name is : Daddy
# Multilevel Inheritance :
# In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

# Example:
# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
 
 
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self, grandfathername)
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self, fathername, grandfathername)
 
#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()
# Output:
# George
# Grandfather name : George
# Father name : Philip
# Son name : Charles
# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# Example:
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
      
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
 
#  object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
# Output:
# This function is in parent class.
# This function is in child 1.
# This function is in parent class.
# This function is in child 2.
# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# Example
# class School:
#     def func1(self):
#         print("This function is in school.")
 
 
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
 
 
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")
 
 
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
 
# object = Student3()
# object.func1()
# object.func2()
# Output:
# This function is in school.
# This function is in student 1.




# class Parent:
#   def fun1(self):
#       print("I am your parent class") 

# class Child(Parent):
#   def fun2(self):
#     print("This function is in child class")

# object = Child()
# object.fun1()
# object.fun2()  




















# Access Specifiers/Modifiers
# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers
# Public access modifier
# Private access modifier
# Protected access modifier



# Public Access Specifier in Python
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

# Example:
# class Student:
#     # constructor is defined
#     def __init__(self, age, name):
#         self.age = age               # public variable
#         self.name = name             # public variable
# obj = Student(21,"Harry")
# print(obj.age)
# print(obj.name)
# Output:
# 21
# Harry














# # calling by object  of class Subject
# print(obj1.__age)
# print(obj1.__funName())
# Output:
# AttributeError: 'student' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# AttributeError: 'subject' object has no attribute '__age'
# AttributeError: 'student' object has no method '__funName()'
# Private members of a class cannot be accessed or inherited outside of class. If we try to access or to inherit the properties of private members to child class (derived class). Then it will show the error.

# Name mangling
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

# class MyClass:
#     def __init__(self):
#         self._nonmangled_attribute = "I am a nonmangled attribute"
#         self.__mangled_attribute = "I am a mangled attribute"
# my_object = MyClass()
# print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
# print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
# In the example above, the attribute _nonmangled_attribute is marked as nonmangled by convention, but can still be accessed from outside the class. The attribute __mangled_attribute is private and its name is "mangled" to _MyClass__mangled_attribute, so it can't be accessed directly from outside the class, but you can access it by calling _MyClass__mangled_attribute




# Protected Access Modifier
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

# It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

# Example:
# class Student:
#     def __init__(self):
#         self._name = "Harry"
#     def _funName(self):      # protected method
#         return "CodeWithHarry"
# class Subject(Student):       #inherited class
#     pass
# obj = Student()
# obj1 = Subject()
# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())
# Output:
# Harry
# CodeWithHarry
# Harry
# CodeWithHarry

















# class Student:
#     def __init__(self):
#         self._name = "Harry"

#     def _funName(self):      # protected method
#         return "CodeWithHarry"

# class Subject(Student):       #inherited class
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)      
# print(obj._funName())     
# # calling by object of Subject class
# print(obj1._name)    
# print(obj1._funName())





















# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
# result = Math.add(1, 2)
# print(result) # Output: 3
# In this example, the add method is a static method of the Math class. It takes two parameters a and b and returns their sum. The method can be called on the class itself, without the need to create an instance of the class.


# class Math:
#   def __init__(self, num):
#     self.num = num

#   def addtonum(self, n):
#     self.num = self.num +n
    
#   @staticmethod
#   def add(a, b):
#       return a + b

# # result = Math.add(1, 2)
# # print(result) # Output: 3
# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# print(Math.add(7, 2)) 














# Instance vs class variables
# In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

# Class Variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

# class MyClass:
#     class_variable = 0
    
#     def __init__(self):
#         MyClass.class_variable += 1
        
#     def print_class_variable(self):
#         print(MyClass.class_variable)
        
# obj1 = MyClass()
# obj2 = MyClass()
# obj1.print_class_variable() # Output: 2
# obj2.print_class_variable() # Output: 2
# In the example above, the class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable.

# Instance Variables
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.

# class MyClass:
#     def __init__(self, name):
#         self.name = name
        
#     def print_name(self):
#         print(self.name)
# obj1 = MyClass("John")
# obj2 = MyClass("Jane")
# obj1.print_name() # Output: John
# obj2.print_name() # Output: Jane
# In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.

# Summary
# In summary, class variables are shared among all instances of a class and are used to store information that is common to all instances. Instance variables are unique to each instance of a class and are used to store information that is specific to each instance. Understanding the difference between class variables and instance variables is crucial for writing efficient and maintainable code in Python.

# It's also worth noting that, in python, class variables are defined outside of any methods and don't need to be explicitly declared as class variable. They are defined in the class level and can be accessed via classname.varibale_name or self.class.variable_name. But instance variables are defined inside the methods and need to be explicitly declared as instance variable by using self.variable_name.









# class Employee:
#   companyName = "Apple"
#   noOfEmployees = 0
#   def __init__(self, name):
#     self.name = name
#     self.raise_amount = 0.02
#     Employee.noOfEmployees +=1
#   def showDetails(self):
#     print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# # Employee.showDetails(emp1)
# emp1 = Employee("Harry")
# emp1.raise_amount = 0.3
# emp1.companyName = "Apple India" 
# emp1.showDetails()
# Employee.companyName = "Google"
# print(Employee.companyName)

# emp2 = Employee("Rohan")
# emp2.companyName = "Nestle"
# emp2.showDetails()














# rst argument of the function is always "cls," which represents the class itself.

# Why Use Python Class Methods?
# Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

# How to Use Python Class Methods
# To define a class method, you simply use the "@classmethod" decorator before the method definition. The first argument of the method should always be "cls," which represents the class itself. Here is an example of how to define a class method:

# class ExampleClass:
#     @classmethod
#     def factory_method(cls, argument1, argument2):
#         return cls(argument1, argument2)
# In this example, the "factory_method" is a class method that takes two arguments, "argument1" and "argument2." It creates a new instance of the class "ExampleClass" using the "cls" keyword, and returns the new instance to the caller.

# It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.

# Conclusion
# Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class. They are useful for creating factory methods, alternative constructors, and other types of methods that operate at the class level. With the knowledge of how to define and use class methods, you can start writing more complex and organized code in Python.








# class Employee:
#   company = "Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")

#   @classmethod
#   def changeCompany(cls, newCompany):
#     cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"
# e1.show()
# e1.changeCompany("Tesla")
# e1.show()
# print(Employee.company)


