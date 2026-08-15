marks=int(input("enter student marks"))
if marks>100 or marks<0:
    print("Invalid input! Marks must be between 0 and 100.")
else:
    if 90<=marks<=100:
        Grade="A+"
        Remark="outstanding"
        Result="Pass"
    
    elif 75<=marks<=89:
        Grade="A"
        Remark="Excellent"
        Result="Pass"
 
    elif 60<=marks<=74:
        Grade="B"
        Remark="Good"
        Result="Pass"
    elif 50<=marks<=59:
        Grade="C"
        Remark="Average"
        Result="Pass"
    elif 40<=marks<=49:
        Grade="D"
        Remark="Pass(needs imporvement)"
        Result="Pass"  
    elif 40>marks:
        Grade="F"
        Remark="Fail"
        Result="Fail"
    else:
        print("invalid marks")

    print("\n")
    print("Marks obtained:",marks)
    print("Grade: ",Grade)
    print("Remark: ",Remark)
    print("Result: ",Result)
