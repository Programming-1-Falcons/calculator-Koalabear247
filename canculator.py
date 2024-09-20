while True:
    num1= float(input("enter a number"))
    math= (input("addition, subtraction, multiplication, division, exponents"))
    num2 = float(input("enter a number"))

    if math== "addition":
        print(num1, "+", num2, "=", num1 + num2)
    elif math == "subtraction":
        print(num1, "-", num2, "=", num1 - num2 ) 
    elif math=="multiplication":
        print(num1, "*", num2, "=", num1 * num2)
    elif math == "division":
        print(num1, "//", num2, "=", num1 / num2)
    elif math =="exponents":
        print(num1, "**", num2, "=", num1** num2)
    else:
        print("syntax error")    