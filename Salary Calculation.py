#program 8
# Salary Calculation

y=int(input("Enter Your Basic Salary:"))
p=int(input("Enter Your HRA Percentage"))
HRA=(p/100)*y
t=int(input("Enter Your Travel Allowence"))
Gross=y+HRA+t
print("Total Gross Salary is:",Gross)
