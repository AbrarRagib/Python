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



import Demo_1

Demo_1.welcome()






