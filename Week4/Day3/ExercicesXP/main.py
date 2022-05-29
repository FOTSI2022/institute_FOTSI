"""
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
del sample_dict["name"]
del sample_dict["salary"]
print(sample_dict)
"""
"""
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print('Welcome to our restaurant\n')
for (fruit, price) in items.items():
    print(f"{fruit}:{price} FCFA")




"""

items = {
    "banana": {"price":4 , "stock":10},
    "apple": {"price":2, "stock":5},
    "orange": {"price":1.5 , "stock":24},
    "pear": {"price":3 , "stock":1}
}
"""
cout=0
for x in items:
    valeur_sauve=1
    for cle, valeur in items[x].items():
        valeur_sauve=valeur*valeur_sauve
    cout=cout+valeur_sauve
print('Le cout total est', cout,'FCFA')

"""
"""
Convert Lists Into Dictionaries
"""
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
keys_values_zip=zip(['Ten', 'Twenty', 'Thirty'],[10, 20, 30])
keys_values_zip_dic=dict(keys_values_zip)
print(keys_values_zip_dic)
"""
"""
A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
ow much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
"""
"""
print('family')
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(family)
print('++++++++++++++++++++++++++++++++++++++')
print('How much does each family member have to pay ?')
for name, age in family.items():
    if age<3:
        price=0
    elif 3<=age<=12:
        price=10
    else:
        price=15
    print(f"{name}:{price} $")
print('++++++++++++++++++++++++++++++++++++++')
print('Print out the family’s total cost for the movies')
cout = 0
for name, age in family.items():
    if age < 3:
        cout += 0
    elif 3 <= age <= 12:
        cout += 10
    else:
        cout += 15
print(f"The total cost for the {len(family)} family is ${cout}")
print('++++++++++++++++++++++++++++++++++++++')

"""
"""
print('Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).')
family2={}
name=""
while name !='exit':
    name=input('Give the name or type exit to stop...')
    if name=='exit':
        print('Goodbye')
        age = ''
    else:
        age = input(f"Give the age of {name}")

    if name!='exit':
        family2[name]=age

print(family2)
"""
"""
print('Exercise 3: Zara')
name: Zara
creation_date: 1975
creator_name: Amancio Ortega Gaona
type_of_clothes: men, women, children, home
international_competitors: Gap, H&M, Benetton
number_stores: 7000
major_color:
    France: blue,
    Spain: red,
    US: pink, green
"""
"""
print('Exercise 3: Zara')
print('++++++++++++++++++++++++++++++++')
print('Create a dictionary called brand which value is the information from part one (turn the info into keys and values).')
brand={}
brand['name']= 'Zara'
brand['creation_date']= 1975
brand['creator_name']= 'Amancio Ortega Gaona'
brand['type_of_clothes']= 'men, women, children, home'
brand['international_competitors']= 'Gap, H&M, Benetton'
brand['number_stores']= 7000
brand['major_color']= {'France': 'blue','brand Spain': 'red', 'US': 'pink, green'}

print(brand)

print('++++++++++++++++++++++++++++++++')
print('Change the number of stores to 2.')
brand['number_stores']=2
print(brand)

print('++++++++++++++++++++++++++++++++')
print('Print a sentence that explains who Zaras clients are')
print('Zaras client are',brand['name'])

print('++++++++++++++++++++++++++++++++')
print('Add a key called country_creation with a value of Spain')
brand['country_creation']='Spain'
print(brand)

print('++++++++++++++++++++++++++++++++')
print('Check if the key international_competitors is in the dictionary. If it is, add the store Desigual')
if 'international_competitors' in brand:
    brand['store'] = 'Desigual'
    brand['number_stores'] +=1
print(brand)

print('++++++++++++++++++++++++++++++++')
print('Delete the information about the date of creation')
del brand['creation_date']
print(brand)

print('++++++++++++++++++++++++++++++++')
print('Print the last international competitor.')
international_competitors=str(brand['international_competitors'])
print(international_competitors)
inter= international_competitors.split(',')
print(inter[-1])

print('++++++++++++++++++++++++++++++++')
print('Print the major clothes colors in the US..')
print(brand['major_color']['US'])

print('++++++++++++++++++++++++++++++++')
print(' Print the amount of key value pairs (ie. length of the dictionary)')
print(len(brand))

print('++++++++++++++++++++++++++++++++')
print('Print the keys of the dictionary.')
for i in brand.values():
    print(i)

print('++++++++++++++++++++++++++++++++')
print('Create another dictionary called more_on_zara with the following details:')
more_on_zara={}
more_on_zara['creation_date']= 1975
more_on_zara['number_stores']=10000
print(more_on_zara)

print('++++++++++++++++++++++++++++++++')
print('Use a method to add the information from the dictionary more_on_zara to the dictionary brand')
brand.update(more_on_zara)
print(brand)

print('++++++++++++++++++++++++++++++++')
print('Print the value of the key number_stores. What just happened ?')
print(brand['number_stores'])
"""
"""
exercice 4
"""

"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
"""
"""
disney_users_A={}
i=0
for user in users:
    disney_users_A[user]=i
    i+=1
print(disney_users_A)

"""
"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
"""
"""
disney_users_A={}
for i in range(0,len(users)-1):
    disney_users_A[i]=users[i]
  
print(disney_users_A)
"""
"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
 print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
"""
"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_D=sorted(users)

disney_users_C={}
i=0
for user in disney_users_D:
    disney_users_C[user]=i
    i+=1
print(disney_users_C)
"""

"""
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
"""
"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={}
i=0
for user in users:
    if 'i' in user:
        disney_users_A[user]=i
        i+=1
print(disney_users_A)
"""
"""
Only recreate the 1st result for:
The characters, which names start with the letter “m” or “p”.
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

"""
"""
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={}
i=0
for user in users:
    if (user[0].lower()=='m') or (user[0].lower()=='p'):
        disney_users_A[user]=i
        i+=
print(disney_users_A)
"""

"""
En cryptographie, un chiffrement de César est l'une des techniques de chiffrement les plus simples et les plus connues.
C'est un type de chiffrement par substitution dans lequel chaque lettre du texte en clair est remplacée par une lettre à un nombre fixe de positions dans l'alphabet.

Par exemple, avec un décalage à gauche de 3 -> D serait remplacé par A,
–> E deviendrait B, et ainsi de suite.

La méthode porte le nom de Jules César, qui l'a utilisée dans sa correspondance privée.

Créez un programme python qui crypte et décrypte les messages avec le chiffrement césar.
L'utilisateur entre dans le programme, puis le programme lui demande s'il veut chiffrer ou déchiffrer, puis exécuter le chiffrement/déchiffrement sur un message donné et un décalage donné.
"""
alphabet=[a,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
print(alphabet)



