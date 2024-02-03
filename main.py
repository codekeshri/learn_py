# str = "codekeshri"
# print(str[1:len(str)])
# print(str[:len(str)])
# print(str[:len(str)-2])
#
# # -ve index in python
#
# print(str[-3: -1])
# print(str.endswith("i"))
# print(str.endswith("9"))
# print(str.capitalize()) #creating a new string
# str = str.capitalize() #modifies the original string
# print(str)
# print(str.replace("e", "a")) #valid for words also
# print(str.find("a")) #valid for words also
# print(str.count("h"))
#
# #write a program to input first name and print its length
# name = input("Enter your name: ")
# print(name)
#
# marks = 74
# print(marks)
# grade = ""
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 70 and marks < 90):
#     grade = "B"
#
# print(grade)

# program for odd even
# a = int(input("Enter the number: "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a, b, c)%7==0)

# arrays = list and tuples
# list can contain different data types
# strings are immutable and lists are mutable in python
# student = ["arvind", 28, 98]
# print(student)
# student[0] = 1
# print(student)
# # print(student[0: 1])
# student.append(8)  # appends but return null
# print(student)
# student.sort()     # returns null but changes the list
# print(student)
# student.sort(reverse=True)
# print(student)
# student.reverse()
# print(student)
# student.insert(2, "app.e")
# print(student)
# student.remove(98)
# print(student)
# student.pop()
# print(student)
# -------------------------TUPLES---------------------------------------------
# tuples are immutable i.e. no assignment or changing operations
tup = (87, 78, 12, 21)
print(type(tup), tup[1])
# empty tuple is also valid
# tup = (1, ) is tuple and tup = (1) is integer in python
# we can slice tuples like strings
print(tup.index(12))
print(tup.count(21))

# ask user to enter 3 movie names and store in a list
one = input()
two = input()
three = input()
movies = [one, two, three]
print(movies)
muvi = movies.copy()
movies.reverse()
print(muvi == movies)

t = ("C", "D", "A", "A", "B", "B", "A")
print(t.count("A"))
g = ["C", "D", "A", "A", "B", "B", "A"]
g.sort()
print(g)

















