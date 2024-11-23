from logininfo import *
from list import *
from genre import*
if name_1 and password_1 : 
    
    print("You have to return the following books:")
    a11 = open('customer1.dat','r')
    print(a11.read())

    r=input("Enter the name of the book you want to return:")
    print("You have returned",r)

elif name_2 and  password_2:
    print("You have to return the following books:")
    a22 = open('customer2.dat','r')
    print(a22.read())
    
    
    p=input("Enter the name of the book you want to return:")
    print("You have returned",p)
    print("Return successful")

elif name_3 and password_3 :
    print("You have to return the following books:")
    a33 = open('customer3.dat','r')
    print(a33.read())
    
    q=input("Enter the name of the book you want to return:")
    print("You have returned",q)
    print("Return successful")

elif name_4 and  password_4 :
    print("You have to return the following books:")
    a44 = open('customer4.dat','r')
    print(a44.read())
    
    s=input("Enter the name of the book you want to return:")
    print("You have returned",s)
    print("Return successful")
else :
    print("****YOU DO NOT HAVE TO RETURN ANY BOOK!!!****")