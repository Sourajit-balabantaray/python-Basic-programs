#program 5
# Simple Interest

princple=int(input("Enter the Princple Value:"))
rate=int(input("Enter the rate of interest:"))
time=int(input("Enter the Time taken in Years:"))
Si=(princple*rate*time)/100
Total=princple+Si
print("Simple interest is:",Si)
print("Total Amount to give is",Total)
