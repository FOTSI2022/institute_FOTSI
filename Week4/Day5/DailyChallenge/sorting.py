"""
sorting
input
without, hello, bag, world
output
bag, hello, without, world
"""
#we get the words
list_word=input("Enter words sperated by a comma...")

#we transform into list of words
list_given= list_word.split(',')

#we sorted we list comprehension
list_sorted=[word for word in sorted(list_given)]
print(list_sorted)

#we print them with join
print(','.join(list_sorted))