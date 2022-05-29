'''
Exercice 1
Ask the user for a number between 1 and 100

If the number is a multiple of three, print "Fizz"

If the number is a multiple of five, print "Buzz".

If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.



#controle de la valeur du nombre saisi
nombre=0

while nombre<1 or nombre>100:
    nombre_saisi=input("Entrer un nombre entre 1 et 100 : ")
    try:
        nombre=int(nombre_saisi)
    except:
        print("Attention!!! Entrez un nombre entre 1 et 100")

#conditions

if nombre % 3==0 and nombre % 5 == 0:
    print('FizzBuzz')
elif nombre % 3 == 0:
    print("Fizz")
elif nombre % 3 == 0:
    print("Buzz")
else:
    print("Not a multiple of 3 or 5")
'''

'''
exercice 
Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

print(f"{(99**3)*8}")


print(('hello world\n'*4)) 
# \n pour le retour 0 lq ligne

'''

'''
exercice 
Exercise 4 : Your Computer Brand
Instructions
Create a variable called computer_brand which value is the brand name of your computer.
Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
'''
'''
def computer_brand():
    my_computer_brand=input("What is the name of your computer brand? ")
    print(f"I have a {my_computer_brand} computer")

computer_brand()
'''
'''
Exercise 5 : Your Information
Instructions
Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code
'''
'''
def information():
    name=input("Your name :")
    age = input("Your age :")
    shoe_size = input("Your shoe_size :")
    info=f"My name is {name}, I am cameroonian, I am {age}. I am born in Yaounde and I shoe {shoe_size}"
    print(info)
information()
'''
'''
Exercise 6 : A & B
Instructions
Create two variables, a and b.
Each variables value should be a number.
If a is bigger then b, have your code print Hello World.
'''
'''
def comparaison():
    a=""
    while a=="":
        a_saisi=input("Give the value of a: ")
        try:
            a=float(a_saisi)
        except ValueError:
            print("You should enter a number")

    b = ""
    while b=="":
        b_saisi = input("Give the value of b: ")
        try:
            b = float(b_saisi)
        except ValueError:
            print("You should enter a number")


    if a>b:
        print("Hello world")
    else:
        print(f"Sorry {a} is not bigger than {b}")
comparaison()

'''
'''
Exercise 7 : Odd Or Even
Instructions
Write code that asks the user for a number and determines whether this number is odd or even.
'''

'''
def odd_even():
    a=""
    while type(a)!=int :
        a_saisi = input("Give the value of the number: ")
        try:
            a = int(a_saisi)
        except ValueError:
            print("You should enter a number...an integer")

    if a%2==0:
        print(f"{a} is a even number")
    else:
        print(f"{a} is a odd number")
odd_even()
'''

'''
Exercise 8 : What’s Your Name ?
Instructions
Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
'''

'''
def ask_name():
    my_name="paul"
    your_name=input("Give your name ...")
    if my_name==your_name:
        print(f"Unbelievable....my name is {my_name} too. We are homonyme")
    else:
        print(f" You have a beautiful name {your_name}. It has {len(your_name)} letters. Mine is {my_name} and has {len(my_name)} ")


ask_name()
'''
'''
Exercise 9 : Tall Enough To Ride A Roller Coaster
Instructions
Write code that will ask the user for their height in inches.
If they are over 145cm print a message that states they are tall enough to ride.
If they are not tall enough print a message that says they need to grow some more to ride.

nb:1 cm = 0.39370079 in 
'''

def ride_roller():
    your_height=""
    while your_height=="":
        your_height_saisi=input("Give us your height in inches")
        try:
            your_height=float(your_height_saisi)
        except ValueError:
            print("You should give a number")
    height_converted= your_height//0.39370079
    print(f"Your height is {your_height} inches which eguals to {height_converted} centimeters ")

    if height_converted>145:
        print("Your are are tall (under 145 cm) enough to ride ")
    else:
        print("You need to grow some more to ride")

ride_roller()