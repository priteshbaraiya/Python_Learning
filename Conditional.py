# conditions examples & statements

light = input("enter traffice light color: ")
if light == "red":
    print("stop")
elif light == "yellow":
    print("Look and wait")
elif light == "green":
    print("Go")
else:
    print("invalid color / light is Broken")

# Output
"""enter traffice light color: red
stop
enter traffice light color: yellow
Look and wait
enter traffice light color: green
Go
enter traffice light color: blue
invalid color / light is Broken"""

# students marks example

marks = input("enter your marks:")
marks = int(marks)
if marks >= 90:
    print("A1 Grade")
elif (marks >= 80 and marks < 90):
    print("A2 Grade")
elif (marks >= 70 and marks < 80):
    print("B1 Grade"  )
elif (marks >= 60 and marks < 70):
    print("B2 Grade")
elif (marks >= 50 and marks < 60):
    print("Last Grade")
else:
    print("Fail")


# Output
"""enter your marks:95
A1 Grade
enter your marks:85
A2 Grade
enter your marks:75
B1 Grade
enter your marks:65
B2 Grade
enter your marks:55
Last Grade
enter your marks:35
Fail"""





# Practice 

A = int(input("A : "))
G = input("M/F : ")

if (A == 1 or A == 2) and G == "M":
    print("fee is 100")

elif (A == 3 or A == 4) or G == "F":
    print("fee is 200")

elif A == 5 and G == "M":
    print("fee is 300")

else:
    print("no fee")

# Output
"""
PS D:\PYTHON_AC> python .\Conditional.py
A : 5  
M/F : M
fee is 300
PS D:\PYTHON_AC> python .\Conditional.py   
enter traffice light color: red
stop
enter your marks:50
Last Grade
A : 2
M/F : F
fee is 200
PS D:\PYTHON_AC> """


# Ternary Operator

drink = input("drink :")
eat = "yes" if drink == "tea" else "no"
print(eat)


# Output
"""PS D:\PYTHON_AC> python .\Conditional.py
drink :tea
yes
PS D:\PYTHON_AC> python .\Conditional.py
drink :coffee
no"""

# End of the code

age = int(input("Enter Age "))
vote = ("yes","no") [age < 18]
print(vote) 

# Output
"""PS D:\PYTHON_AC> python .\Conditional.py
Enter Age 18
yes
PS D:\PYTHON_AC> python .\Conditional.py
Enter Age 16
no"""