amount = int(input("Enter purchase amount: "))
membership = input("Enter membership (regular/silver/gold/platinum): ").lower()

discount_percentage = 0

if membership == "regular":
    discount_percentage = 5
elif membership == "silver":
    discount_percentage = 10
elif membership == "gold":
    discount_percentage = 15
elif membership == "platinum":
    discount_percentage = 20
else:
    print("Error: Invalid membership type entered!")
    exit()


if amount < 500:
    discount_percentage = 0.00
    discount_amount = 0.00
    delivery_charge = 50.00
    final_amount = amount - discount_amount + delivery_charge
    print("\n")
    print("Discount Percentage:", discount_percentage, "%"," (amount below Rs 500)")
    print("Delivery Charge:", delivery_charge)
    print("Final Payable Amount:", final_amount)
else:
    delivery_charge = 50.00
    discount_amount = amount * discount_percentage / 100

    if amount > 10000:
        discount_amount += 500.00
        delivery_charge = 0.00
        

    final_amount = amount - discount_amount + delivery_charge

    print("\nPurchase Amount:", amount)
    print("Membership Type:", membership.capitalize())
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount:", discount_amount)
    print("Delivery Charge:", delivery_charge)
    print("Final Payable Amount:", final_amount)
