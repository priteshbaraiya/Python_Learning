# Our First Program
print("Hello World !")

# print is a input function 
print("Frist Programm Done")
age = input("Enter Your Age:")
print("your Age Is : "+ age)
print(20+10)


# VARIABLES DECLARED AND UNDERSTAND THROW BELOW EXAMPLE 

name = "BUNTY" # string (word , centence , multiple line) 
age = 20       # intinger 
price = 20.2  # float(decimle number )

print("My Name Is : ",name )    
print("My age Is : ",age  )    

b = 10
a = b 
print(a)
print(b)


print(type(name))
print(type(age))
print(type(price))  


# single , double , triple Quotes Are Valid 

name = 'PR'
name1 = "PR"
name2 = '''PR'''

print(name)
print(name1)
print(name2)

old = False 
b = None 

print(type(old))
print(type(b))


# print sum of 2 numbers

a = 5000
b = 1000
diff= a - b
print(diff)

a,b = 2,3
c = 4
txt = "@"
print(a*txt*b)
print((a + txt)*b)

print(a+b*4)

#arithmetic oprater with integer & float will result in float 👇

a,b = 10,5.0
c = a*b
print(c)
print(type(c))

#intiger division 

a,b = 12 , 5
c = a//b
print(c)
print(type(c))