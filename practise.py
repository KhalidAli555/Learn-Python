# with open("practise.txt","w") as f:
#     f.write("i everyone\n we are learning file I/O\n")
#     f.write("using Java\nI like Programming in Java.")


#practise question
# with open("practise.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)

# with open("practise.txt","w") as f:
#     f.write(new_data)

#practise question

# with open("practise.txt","r") as f:
#     data=f.read()
# if(data.find("learning") != -1):
#     print("word found")
# else:
#     print("word Not found")

#*****************************************

# def sum(a,b):
#     s=a+b
#     print(s)
#     return s
# sum(10,20)
# sum(20,30)

# #or

# def cal_sum(a,b):
#     return a+b
# sum=cal_sum(20,5)
# sum=cal_sum(100,50)
# print(sum)

# def cal_avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg
# cal_avg(10,20,30)


#WAF to print the length of the list
# cities=["karachi","islamabad","lahore","peshawar","multan"]
# def print_len(cities):
#     print(len(cities))

# print_len(cities)

# #WAF to print the list of item in single line
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(cities)

#WAF to calculate the factorial of number
# def cal_factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)

# cal_factorial(6)

# 
#WAF to convert PKR to USD 
# def converter(usd_val):
#     pak_val=usd_val*280
#     print(usd_val,"USD=", pak_val,"PKR")
# converter(20)      #function calling


#classes (OOP)

# class Student():
#     name="khalid ali"

# s1=Student()
# print(s1.name)
#************************************
# class Cars():
#     color="blue"
#     brand="mercedes"
# c1=Cars()
# print(c1.color)
# print(c1.brand)
#**********************************
# class Student():
#     college_name="Hecon college"
#     #Parameterized constructor
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#         print("adding new student in database")
# s1=Student("khalid ali",89)
# print(s1.name,s1.marks)
# print(s1.college_name)

# s2=Student("Anaya Ali",98)
# print(s2.name,s2.marks)
# print(s2.college_name)

#**********************
# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("welcome students")
#     def get_marks(self):
#         return self.marks
# s1=Student("khalid ali",98)
# print(s1.name,s1.marks)
# s1.welcome()
# print(s1.get_marks())

#***********practise question*************
# class Student():
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"YOur  avg marks is",sum/3)

# s1=Student("khalid", [78,98,80])
# s1.get_avg()

#*************static method(not take self parameter)**********
# class Student():
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def Hello():
#         print("hello students")
# s1=Student("khalid")
# print(s1.name)
# s1.Hello()

#***********Abstruction********
# class Car:
#     def __init__(self):
#         self.acceletor=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acceletor=True
#         print("car started")

# car1=Car()
# car1.start()
#*******inheritance*******

# class Car:
#     color="blue"
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name
# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("priuris")      
# print(car1.name)
# print(car1.start())        #inherit start method from car class
# print(car1.color)           #inherit color property from car class

#****multilevel inheritance*****
# class Car:
#     color="blue"
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand
 
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type

# car1=Fortuner("disel")
# print(car1.start(),car1.type)

#*****multilevel inheritance****
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varc="welcome to class C"

carC=C()
print(carC.varc)
print(carC.varA)
print(carC.varB)


