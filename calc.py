print("select an operation which you want to perform:")
print("1.ADD")
print("2.SUBTRACTION")
print("3.MULTIPLY")
print("4.DIVIDE")
operation = input("the operation you have choosed is  = ")


if operation == "1":
    num1 = input("ENTER FIRST NUMBER:")
    num2 = input("ENTER SECOND NUMBER:")
    num3 = input("ENTER THIRD NUMBER:")
    print("the sum is "+str(int(num1)+int(num2)+int(num3)))
elif operation == "2":
    num1 = input("ENTER FIRST NUMBER:")
    num2 = input("ENTER SECOND NUMBER:")
    num3 = input("ENTER THIRD NUMBER:")
    print("the subtraction is " + str(int(num1) - int(num2) - int(num3)))
elif operation == "3":
    num1 = input("ENTER FIRST NUMBER:")
    num2 = input("ENTER SECOND NUMBER:")
    num3 = input("ENTER THIRD NUMBER:")
    print("the multiplication is " + str(int(num1) * int(num2) * int(num3)))
elif operation == "4":
    num1 = input("ENTER FIRST NUMBER:")
    num2 = input("ENTER SECOND NUMBER:")
    num3 = input("ENTER THIRD NUMBER:")
    print("the divison  is " + str(int(num1) / int(num2) / int(num3)))
