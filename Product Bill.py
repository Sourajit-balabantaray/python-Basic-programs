#program 11
# Product Bill

y=input("Product name:")
q=int(input("Enter Quantity:"))
p=int(input("Enter price of a product:"))

sub=q*p
tax=sub*(0.05)
final=sub+tax

print("The Subtotal is:",sub)
print("Total Tax is:",tax)
print("Total Amount is:",final)
