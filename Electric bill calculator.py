units = int(input("Enter units consumed: "))

bill = 0


if units <= 100:
    bill = units * 2.00
elif units <= 200:
    bill = (100 * 2.00) + ((units - 100) * 3.50)
elif units <= 300:
    bill = (100 * 2.00) + (100 * 3.50) + ((units - 200) * 4.50)
else:
    bill = (100 * 2.00) + (100 * 3.50) + (100 * 4.50) + ((units - 300) * 6.00)

slab_bill = bill


if bill < 200:
    bill = 200
    print(f"Units Consumed : {units}")
    print(f"Bill Before Discount : Rs {bill:.2f} (min. bill applied, slab-wise bill was Rs {slab_bill:.2f})")
    discount = 0
else:
    
    if units <= 300:
        discount = 0
    elif units <= 500:
        discount = bill * 0.05
    else:
        discount = bill * 0.10

    print(f"Units Consumed : {units}")
    print(f"Bill Before Discount : Rs {bill:.2f}")

print(f"Discount Amount : Rs {discount:.2f}")

final_bill = bill - discount
print(f"Final Payable Amount : Rs {final_bill:.2f}")
