"""Exercice
def calculation():
    a=int(input('Entrer le nombre a ...'))
    b = int(input('Entrer le nombre b ...'))

    print(f"Soustraction.... {a}-{b}:={(a-b)}")
    print(f"addition... {a}+{b}:={(a+b)}")
calculation()

"""
"""
Exercice 1
Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
Call the function, and make sure the message displays correctly.
"""
"""
def display_message():
    print('Today your learn Coding in this course')
display_message()
"""

"""
Exercice 2
Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function.
"""
"""
def favorite_book(title):
    print(f"One of my favorite books is <{title}>")
favorite_book("Avengers")
"""
"""
Exercice 3
Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.
"""
def describe_city(name):
