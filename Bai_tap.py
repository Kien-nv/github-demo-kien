#type cast = convert to anthor data
# import math
# d= math.sqrt(400)
# b=-100
# a=3
# c=100

# print("Max: ",int((max(a,b,c,d))))
# print("Min:",int((min(a,b,c,d))))
# x = "13"
# y = int(x)
# print(y)

#__________ print name from input 
 
# name= input ("what your name ?")
# print("hello "+name)
# age= int(input ("How old are you ")) 
# print("Your age is: ",age)

#-------------
# import math
# pi =3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(math.pow(pi,1))
# print(math.sqrt(pi))

#_____________

# name= "Nguyen Van Kien"
# print(name[0::])

#__________IF and elif

# tem=int(input("what is temparature today: "))
# if tem >0 and tem < 30:
#     print("Today is funny whether day")
#     print("Let's go outside")
# elif tem<0 or tem >30:
#     print("Today not have good whether")
#     print(" Stay inside")

#_____________while and while loop

# name=""
# while len(name)==0:
#     name=input("What is your name: ")
# print("Your name is:", name)
# name= None
# while not name :
#     name = input("Enter your name: ")
# print("hello",name)

# for i in "kien ou kien":
# #     print(i)
# import time


# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)
# print("Happy New Year")

# row=(input("how many rows "))
# column= (input("how many columme "))
# symbol= input("what is your symbol ")
# for i in range (row):
#     for i in range (column):
#         print(symbol,end='')
#     print()

# dinner = ["cake","chocopie","cheese"]
# drink = ["sode","cofe","tea"]
# dessert = ["cake","cream","ice"]
# food= [dinner,drink,dessert]
# print(food[0][1])
# print(dinner.count("chocopie"))

# utensils = {"fork", "dish", "knife"}
# utensils.add("napkin I Love you")
# utensils.remove("fork")

# for x in utensils:
#     print(x)
# thudo = {'use': 'washing ton', 'VN': 'Hanoi','Thailand':'bangcok','china':'backinh'}

# thudo.update({'use':'kien'})
# thudo.clear()
# # print(thudo['use'])
# print(thudo)
# name="kien nguyen"
# ten="kien nguyen"
# ten_ho=name[2:]
# Ten_that=ten[:4]
# print(ten_ho)
# print(Ten_that)
# print(type(name))


# def love():
#     print("I love you")
# sex=input("what your sex girl/boy?")
# if sex=="girl":
#     love()
# else:
#     print("bye bye")
# def timX(a,b,c):
#     x= ((pow(a,3)-2*a*b)/(2*b))
#     print("tao ko biet tinh")
# a=int(input("nhap a: "))
# b=int(input("nhap b"))2
# c=int(input("nhap c"))
# timX(a,b,c)
# tham_so ="abc"
# for i in tham_so:
#     i=int(input("nhap ",i))

# def hello(first,midle,last):
#     print("hello "+first+" "+midle+" "+last)

# hello(first="kien",last="nguyen",midle="van")
# def tich(a,b):
#     c = a*b
#     return c
# print(tich(2,1111111))
 
# num = input("nhap so vao day tao xu ly cho dm")
# num = float(num)
# print(num)
# def add(*args):
#     for i in args:
#         print(i,end='')
# add("I love you","love")



# def add(**ar):
#     for k,v in ar.items():
#         print(v,end='')
# add(a="kien",b="nguyen")

# animal = "dog"
# item = "cogi"
# money= 112.222
# print("the {} specise is {}, and It prices {:f}".format(animal,item,money))

# import random

# x = random.randint(1,2)
# y = random.random()
# print(x)

# myList = ['rock','paper','scissor']
# z = random.choice(myList)
# print(z)
# cards = [1,2,3,4,5,6,7,8,9,"j","q","k"]
# random.shuffle(cards)
# print(cards)
# try:
#     numerator = int(input("Enter a number to divice:"))
#     denominator = int(input("Enter a number to divece by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("you can't divide by zero ! idiot !")
# except ValueError as e:
#     print(e)
#     print("Enter only number plz")
# except Exception as e:
#     #print()
#     print("something when wrong ")
# else:
#     print(result)




# # file detection in python
# import os
# path = "C:\\Users\\Setup\\Desktop\\kien"

# if os.path.exists(path):
#     print("that location exist")
#     if os.path.isfile(path):
#         print("that is file")
#     elif os.path.isdir(path):
#         print("that is a directory")
# else:
#     print("that location doesn't exist")

# try:
#     with open('C:\\Users\\Setup\\Desktop\\kien\\test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file is not found")

# text ='hello, i love you Bich Ngoc'
# with open('D:\\Code exam\\kient','w') as file:
#     file.write(text)

# import os
# import shutil

# path = "D:\\Code exam\\kient.txt"

# try:
#     os.remove(path)
# except FileNotFoundError:
#     print('file not found')
# except PermissionError:
#     print("You not have permission for that")
# else:
#     print(path,"was deleted")

# import random
# # from secrets import choice
# # from types import NoneType
# while True:
#     choice= ["rock","paper","scissor"]
#     computor= random.choice(choice)
#     player = None
#     while player not in choice:
#         player= input("slect form rock, paper, scissor: ").lower()
#         if player==computor:
#             print("computor:",computor)
#             print("Your choice:",player)
#             print( "You tie!")
#         elif player=="rock":
#             if computor=="paper":
#                 print("computor:",computor)
#                 print("Your choice:",player)           
#                 print("You Lose!")
#             else :
#                 print("computor:",computor)
#                 print("Your choice:",player)
#                 print("you win")
#         elif player=="paper":
#             if computor=="scissor":
#                 print("computor:",computor)
#                 print("Your choice:",player)
#                 print("You Lose!")
#             else :
#                 print("you win")
#         elif player=="scissor":
#             if computor=="rock":
#                 print("computor:",computor)
#                 print("computor:",player)
#                 print("You Lose!")
#             else :
#                 print("you win")
#     play_again =  input("Play again (yes/no) ? ").lower()
#     if play_again!= "yes":
#         break
# print(" bye bye")

# def list(a):
#     return[a[0],a[len(a)-1]]

# list([5,4,8]) 
# def tinh_tong(b):
#    tong = 0
#    i=0
#    for i in range(b):
#        tong = tong+ i
#    print(tong)
# tinh_tong(10)
# tính số nguyen tố
#---------------------------- tinh số fibonaci thứ n

# from re import A
# from selectors import EpollSelector


# def fib(n):
#     fn,f1,f0=1,1,0
#     if n<=0:
#         print("nhap so nguyen duong thoi thang lol")
#         pass
#     elif n==1:
#         print("so fibonaci can tim la:",n)
#     else:
#         i=2
#         while (i<=n):
#             fn=f0+f1
#             f1=fn
#             f0=f1
#             i=i+1
#         print("So fibonaci can tim là: ",fn)
    
# fib(2)

#---------------------------- tinh số fibonaci thứ n băng đệ quy
# def fib(n):
#     if n==0:
#         f=0
#         return f
#     elif n==1:
#         f=1
#         return f
#     else:
#         f=fib(n-1)+fib(n-2)
#         return f
# a= fib(4)
# print(a)

# --------------------dictionary

# dictCar = {
#     "brand": "Honda",
#     "model": "Honda Civic",
#     "year": 1972
# }
# for i in dictCar:
#     print(i, ": ", dictCar.get("year"))

# ------------tinh giai thua băng đệ quy


# def gt(n):
#     if n==0:
#      return 1
#     else:
#         return n*gt(n-1)
# n= int(input("nhap so can tinh giai thua vào đay: "))

# print("gia thua của",n,"la",gt(n))

# ------------tinh giai thua bằng vòng lặp

# n=int(input("nhap so nguyen can tinh vao day em oi:"))
# gt,i=1,1
# if n==0:
#     print(" Giai thua la 1")
# else:
#     while(i<=n):
#         gt=gt*i
#         i+=1
#     print("Giai thua cua",n,"la",gt)


# ----------chuoi trong xâu
# gt="kien tien sinh"
# x=''
# print(len(gt))
# for i in range(len(gt)):
#     print(i,end='')
#     x+=gt[len(gt)-1-i]
# print(x)

# # ----------dảo ngược chuỗi
# a="ABCDCBA"
# a=str(a)
# a1=a[::-1]
# if a==a1:
#     print("giong nhau")
#     print(a)
#     print(a1)
# else:
#     print("cha giong nhau")
#     print(a)
#     print(a1)

# -------------------------
# #Initial list
# res = []
#
# # Input lengths
# lengths = int(input("nhập số vào đây"))
#
# # Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input("nbhap so vào đaya"))
#     res.append(n)
#
# def evenNum(res):
#     for i in res:
#         if i%2!=0:
#             res.remove(i)
#         else:
#             continue
#     print(res)
# evenNum(res)
# chương trinh giai phuyong trinh bạca 2
# import math
#
# a= int(input("nhap a: "))
# b= int(input("nhap b: "))
# c= int(input("nhap c: "))
#
# def gpt(a,b,c):
#     d= b*b-4*a*c
#     if d==0 :
#         x1=-b/(2*a)
#         print("Phuong trinh co 2 nghiem bang nhau x1=x2=",x1)
#     elif d>0:
#         t = math.sqrt(d)
#         x1= (-b+t)/(2*a)
#         x2=(-b-t)/(2*a)
#         print("Phuong trình có 2 nghiệm phân biệt x1=", x1, " x2=", x2)
#     else:
#         print("Phuong trinh vo nghiem")
# gpt(a,b,c)
#  phuong trinh phan tích số nguyên dương N thành các thưa soos nguyên tố
# n= int(input("nhap so n: "))
#
# def UNN(n):
#     dem=0
#     for i in range(2, (n+1)):
#         if n%i==0:
#             dem=dem+1
#             print(i, end='')
#             m=n//i
#             if m!=1:
#                 print("*", end='')
#                 UNN(m)
#             break
# UNN(n)
# # tạo một class chứa ít nhất 2 method
# class input_output:
#     def __init__(self):
#         self.s=""
#     def get_string(self):
#         self.s=input("Nhap chuoi vao day ban oi: ")
#     def printout_string(self):
#         print(self.s.lower())
# kien=input_output()
# kien.get_string()
# kien.printout_string()
# print("OK CHƯA EM ƠI")
# class nhan_vien(object):
#     def __init__(self,name,salary,dept):
#         self.name = name
#         self.salary = salary
#         self.dept = dept
#     def p_name(self):
#         print("Name: ", self.name)
#     def p_salary(self):
#         print("Salary: ", self.salary)
#         return self.salary
#     def p_dept(self):
#             print("Dept: ", self.dept)
# NV_A = nhan_vien('Kien',1000,'Dev')
# NV_A.p_name()
# print("Anh ay co muc luong thu viec là: ",NV_A.p_salary())

# ------------chuong trinh sap xep day so----------------
n=int(input("nhap chieu dai day so n: "))
l=[]
for i in range(n):
   m=input("nhap vào so nguyen: ")
   l.append(m)
print("Day so da nhap la: ",l)