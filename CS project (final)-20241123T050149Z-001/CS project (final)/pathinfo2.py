from datetime import *
print('PRESS(1) TO ISSUE')
print('PRESS(2) TO RETURN')
print('PRESS(0) TO EXIT')
x=int(input())

if x==1:
    
    from genre import *
    print('''                                /'\/'\WELCOME TO THE THE AUTHOR'S LIBRARY/'\/'\
        GENRE LIST:
        1. Action
        2. Mystery
        3. Sci_fi
        4. Romance
        5. Horror
        6. Fantasy
        7. Biography''')


    c=int(input('Enter the genre number from the list:'))
    
    n = [] 
    select= int(input('how many books would u like to rent?(feel free to choose any!):'))

    def actionbooks():
        print('The available books in this genre :')
        f=open('action.dat', 'r')
        print(f.read())
    def mysterybooks():
        print('The available books in this genre :')
        f1=open('mystery.dat', 'r')
        print(f1.read())
    def scifibooks():
        print('The available books in this genre :')
        f2=open('sci_fi.dat', 'r')
        print(f2.read())
    def romancebooks():
        print('The available books in this genre :')
        f3=open('romance.dat', 'r')
        print(f3.read())      
    def horrorbooks():
        print('The available books in this genre :')
        f4=open('horror.dat', 'r')
        print(f4.read())
    def fantasybooks():
        print('The available books in this genre :')
        f5=open('fantasy.dat', 'r')
        print(f5.read())
    def biographybooks():
        print('The available books in this genre :')
        f6=open('biography.dat', 'r')
        print(f6.read())
    def Else() :
        print("Please enter a proper value!!!")
    {
        1 : actionbooks(),
        2 : mysterybooks(),
        3 : scifibooks(),
        4 : romancebooks(),
        5 : horrorbooks(),
        6 : fantasybooks(),
        7 : biographybooks()
        } 
        

elif x ==2 :
    from returnbook import *
elif x == 0 :
    exit
    ab = open ('endfile.dat' , 'r')
    print(ab.read())
else :
    print("ENTER A VALID VALUE !!!")

for i in range(select):
    book_num =  int(input('Enter_Book_number:'))
    from genre import *
    from logininfo import *
    if name_1 and password_1 :
        c1= open('customer1.dat','w')
        c1.write(action[book_num] ,('''br'''))
        c1.write(mystery[book_num] ,('''br''') )
        c1.write(sci_fi[book_num] ,('''br'''))
        c1.write(romance[book_num] ,('''br'''))
        c1.write(horror[book_num],('''br''') )
        c1.write(Fantasy[book_num] ,('''br'''))
        
                
    elif name_2 and password_2 :
        c2= open('customer2.dat','w')
        c2.write(action[book_num] ,('''br'''))
        c2.write(mystery[book_num],('''br''') )
        c2.write(sci_fi[book_num] ,('''br'''))
        c2.write(romance[book_num],('''br'''))
        c2.write(horror[book_num],('''br'''))
        c2.write(Fantasy[book_num],('''br'''))
        


    elif name_3 and password_3 :
        c3= open('customer3.dat','w')
        c3.write(action[book_num],('''br'''))
        c3.write(mystery[book_num],('''br'''))
        c3.write(sci_fi[book_num],('''br'''))
        c3.write(romance[book_num],('''br'''))
        c3.write(horror[book_num],('''br'''))
        c3.write(Fantasy[book_num],('''br'''))
        
                
                
    elif name_4 and password_4 :
        c4= open('customer4.dat','w')
        c4.write(action[book_num],('''br'''))
        c4.write(mystery[book_num],('''br'''))
        c4.write(sci_fi[book_num],('''br'''))
        c4.write(romance[book_num],('''br'''))
        c4.write(horror[book_num],('''br'''))
        c4.write(Fantasy[book_num],('''br'''))
        
                
x = ()
a = int(input('''       **Press 1 to issue more books.**
                        **Press 2 to continue.** 
                                                :'''
                       
))

while a == 1 :
    
    from genre import *
    print('''
            GENRE LIST:
            1. Action
            2. Mystery
            3. Sci_fi
            4. Romance
            5. Horror
            6. Fantasy
            7. Biography''')


    c=int(input('Enter the genre number from the list:'))
    def actionbooks():
        print('The available books in this genre :')
        f=open('action.dat', 'r')
        print(f.read())
    def mysterybooks():
        print('The available books in this genre :')
        f1=open('mystery.dat', 'r')
        print(f1.read())
    def scifibooks():
        print('The available books in this genre :')
        f2=open('sci_fi.dat', 'r')
        print(f2.read())
    def romancebooks():
        print('The available books in this genre :')
        f3=open('romance.dat', 'r')
        print(f3.read())     
    def horrorbooks():
        print('The available books in this genre :')
        f4=open('horror.dat', 'r')
        print(f4.read())
    def fantasybooks():
        print('The available books in this genre :')
        f5=open('fantasy.dat', 'r')
        print(f5.read())
    def biographybooks():
        print('The available books in this genre :')
        f6=open('biography.dat', 'r')
        print(f6.read())
    def Else() :
        print("Please enter a proper value!!!")
    
    {
        1 : actionbooks(),
        2 : mysterybooks(),
        3 : scifibooks(),
        4 : romancebooks(),
        5 : horrorbooks(),
        6 : fantasybooks(),
        7 : biographybooks()
        }    
   
    if c== 1 or 2 or 3 or 4 or 5 or 6 or 7:
            select= int(input('how many books would u like to rent?(feel free to choose any!):'))
            i=int(0)
            for i in range(select):
                int(input('Enter_Book_number:'))
                
    else :
        print('ENTER A VALID GENRE !!!')

                
    input2 = int(input(''' **Press 1 to issue more books.**
                             **Press 2 to continue.**'''))
    if input2 == int(2) :
        if name_1 and password_1:
            c11 = open('customer1.dat','r')
            print("You have issued :")
            print(c11.read())
        elif name_2 and password_2:
            c22 = open('customer2.dat','r')
            print("You have issued :")
            print(c22.read())
        elif name_3 and password_3:
            c33 = open('customer3.dat','r')
            print("You have issued :")
            print(c33.read())
        elif name_4 and password_4 :
            c44 = open('customer4.dat','r')
            print("You have issued :")
            print(c44.read())
        break               

if a == 2 :
        if name_1 and password_1:
            c11 = open('customer1.dat','r')
            print("You have issued :")
            print( c11.read())
        elif name_2 and password_2:
            c22 = open('customer2.dat','r')
            print("You have issued :")
            print(c22.read())
        elif name_3 and password_3:
            c33 = open('customer3.dat','r')
            print("You have issued :")
            print(c33.read())
        elif name_4 and password_4:
            c44 = open('customer4.dat','r')
            print("You have issued :")
            print(c44.read())
    
