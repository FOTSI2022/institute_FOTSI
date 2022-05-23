'''
Exercise 3 : Outputs
'''
#true
print(3 <= 3 < 9)

#true
print(3 == 3 == 3)

#False
print(bool(0))

#true
print(bool(1))

#true tous les nombres sont les trues
print(bool(2))


#false
print(bool(5 == "5"))

#true
print(bool(4 == 4) == bool("4" == "4"))

#false
print(bool(bool(None)))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)



