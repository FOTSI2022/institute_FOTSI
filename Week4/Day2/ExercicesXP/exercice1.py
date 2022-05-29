'''
Exercise 1 : Set
Instructions
Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.+

my_fav_numbers={1,2,3,4,5}
print(my_fav_numbers)
print(type(my_fav_numbers))

my_fav_numbers.add(6)
print(my_fav_numbers)

my_fav_numbers.remove(6)
print(my_fav_numbers)

my_fav_numbers.add(7)
print(my_fav_numbers)
print(type(my_fav_numbers))

#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
friend_fav_numbers={'elvi', 'eric', 'xavier', 'paul', 'blaise'}
print(friend_fav_numbers)

my_fav_numbers={1,2,3,4,5}
print(my_fav_numbers)
con=friend_fav_numbers|my_fav_numbers
print(con)

'''

'''
Exercise 2: Tuple
Instructions
Given a tuple which value is integers, is it possible to add more integers to the tuple?

my_tuple=(1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
""" No, it is not possible to add more integers to the tuples"""
'''

'''
Exercise 3: List
Instructions
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)
'''
'''
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
print()

print(f"Remove “Banana” from the list.")
basket.remove("Banana")
print(basket)
print()

print(f"Add “Kiwi” to the end of the list. ")
basket.append("kiwi")
print(basket)
print()

print(f"Add “Apples” to the beginning of the list.")
basket.insert(0,"Apples")
print(basket)
print()

print(f"Count how many apples are in the basket.")
print(basket)
print(f"The list has  {len(basket)} elements")
print()

print(f"Empty the basket and print")
print(basket)
basket=[]
print(basket)
'''
'''
Exercise 4: Floats
Instructions
Recap – What is a float? What is the difference between an integer and a float?
Can you think of another way to generate a sequence of floats?
Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
'''
'''
print("Float are numbers with decimal part. The can be positive or negative. Integers are positive number without decimal part")
print("To generate a sequence of floats we can use the module random")
import random
numbers=[]
for i in range(1,100):
    numbers.append(random.random()*10)
print(f"{numbers}")

print("Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).")
liste=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(liste)
print(type(liste))
'''
'''
Exercise 5: For Loop
Instructions
Use a for loop to print all numbers from 1 to 20, inclusive.
Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
'''
'''
print("print all numbers from 1 to 20, inclusive.")
i=1
while i<=20:
    print (i)
    i+=1

print("even number between 1 and 20")
for element in range(1,21):
    if element%2==0:
        print(element)
'''
'''
Exercise 6 : While Loop
Instructions
Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
'''
'''
my_name='elvis'
your_name=''
while your_name != my_name:
    your_name=input(f"My name is {my_name}.Give me your name...")
    print(f"Last name given...{your_name}")
    if your_name==my_name:
        print('we have the same name {my_name}......Goodbye')
'''
'''
Exercise 7: Favorite Fruits
Instructions
Ask the user to input their favorite fruit(s) (one or several fruits).
Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
Store the favorite fruit(s) in a list (convert the string of words into a list of words).
Now that we have a list of fruits, ask the user to input a name of any fruit.
If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

'''
'''
favorite_fruit=[]
string_fruits=input("Give me your favorite fruits...seprate them with a single space...")

#cette lettre va me permettre de reconstituer les fruits saisis un à un
letter=""
for i in string_fruits:
    #Nous sommes entrain de parcourir le nom du fruit saisi
    if i !=" ":
        #print(i)
        letter=letter+i
    else:
        print(f"leter:{letter}")
        #On a rencontré un espace vide marquant la séparation avec le prochain fruit donné
        favorite_fruit.append(letter)
        #on enregistre le nom complet du premier fruit"""
        letter = ""
        # """on rénitialise la letter pour prendre le prochain fruit"""

#GESTION DU DERNIER CAS
favorite_fruit.append(letter)

print('liste des fruits favoris saisis')
print(favorite_fruit)

a_fruit=input("Please choose a fruit.....")
if a_fruit in favorite_fruit:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
'''

'''
Exercise 8: Who Ordered A Pizza ?
Instructions
Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
'''
'''
def garniture_pizza():
    list_garniture=[]
    garniture=""

    while garniture != 'quit':
        garniture=input('Entrer une garniture ^pour la pizza ou <<quit>> :...')
        print(f"vous avez ajouté la garniture <<{garniture}>> dans la pizza")
        list_garniture.append(garniture)

    print('The all toppings are:')
    for element in range(0,len(list_garniture)-1):
        print(list_garniture[element])

    print(f"The total cost is {10+2.5*len(list_garniture)}")

garniture_pizza()
'''
'''
Exercise 9: Cinemax
Instructions
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.
Ask a family the age of each person who wants a ticket.
Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.
'''
'''
def cinemax():
    print("""   Ticket Prices
          if a person is under the age of 3, the ticket is free.
          if they are between 3 and 12, the ticket is $10.
          if they are over the age of 12, the ticket is $15.
          """)
    age_person=""
    age_person_list=[] # liste des ages consolidés
    i=1
    while age_person != 10000:
            age_person_saisi = input(f"Enter the age of the family member  number {i}...or type <<10000>> to stop...")
            try:
                age_person=int(age_person_saisi) #conversion de age
                age_person_list.append(age_person)  #enregistre age
                i+=1  #incremente i
            except:
                print(f" age de member number {i} doit être un entier positif....or type <<exit>> to stop")

    # sortie de la boucle et calcul du montant
    cout=0
    for age in age_person_list:
        if age<3:
            cout+=0
        elif 3<=age<=12:
            cout += 10
        else:
            cout += 15
    print(f"The total cost for the {len(age_person_list)-1} family is ${cout}") #-1 pour exclure le cqs 10000
cinemax()
'''
'''
def cinemax2():
    print("""   A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
             Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
             At the end, print the final list.
          """)
    names={'alex':"", 'xavier':'', 'paul':'', 'arlin':'', 'olivier':'',}

    #affichage
    for name in names:
        print(name)

    # entrer les valeurs de age
    for name in names:
            names[name]= int(input(f"Entrer l'age de {name}..."))

    # affichage
    print(names)

    names2={} # creqtion nouvelle liste
    for name in names:
        if names[name]>= 16:
            names2[name]=names[name]

    print(names2) # affichage nouvelle liste


cinemax2()
'''

'''
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
Use the above list called sandwich_orders.
Make an empty list called finished_sandwiches.
As each sandwich is made, move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
'''
'''
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches=[]

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")
'''

'''
Exercise 11 : Sandwich Orders#2
Instructions
Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandwiches.
'''
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

sandwich_orders.insert(2,sandwich_orders[-1])
print(sandwich_orders)

sandwich_orders.insert(0,sandwich_orders[-1])
print(sandwich_orders)

print('*********************************')
print(' the deli has run out of pastrami')
print(sandwich_orders)

print('*********************************')
i=0
while i<=len(sandwich_orders):
    if sandwich_orders[i]=="Pastrami sandwich":
        sandwich_orders.remove(sandwich_orders[i])
    i+=1
print(sandwich_orders)


