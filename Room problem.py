#program 12
# Room problem

l=int(input("Enter Length in meter:"))
b=int(input("Enter Breadth in meter:"))
c=int(input("Enter the cost per Square Meter:"))
area=l*b
perimeter=2*(l+b)
cost=c*area
print("Area of the classroom is ",area)
print("Perimeter of the classroom is ",perimeter)
print("Total cost for  the classroom is ",cost)

print(f"area is {area} perimeter is {perimeter} and cost is {cost}")
