'''
Exercice 1
Exercise 1 : Hello World-I Love Python
Instructions
Print the following output in one line of code:
Hello world
Hello world
Hello world
Hello world
I love python
I love python
I love python
I love python
'''

'''

print(('hello world\n'*4)+('I love python\n'*4))
# \n pour le retour 0 lq ligne
'''

'''
Exercise 2 : What Is The Season ?
Instructions
Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
'''

def season():
    month_number=""

    while (month_number=="") or not(1<=month_number<=12):
        month_number_saisi=input("Give me the number of the month and I will give you the season.....")
        try:
            month_number=int(month_number_saisi)
        except:
            print(f"Vous devez entrer un nombre entier compris entre 1 et 12 <<{month_number}>> n'est pas correct")

    if 3<=month_number<=5:
        print(f" The month {month_number} corresponds to SPRING")
    elif 6<=month_number<=8:
        print(f" The month {month_number} corresponds to SUMMER")
    elif 9 <= month_number <= 11:
        print(f" The month {month_number} corresponds to AUTUMN")
    else:
        print(f" The month {month_number} corresponds to WINTER")
season()