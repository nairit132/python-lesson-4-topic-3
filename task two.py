try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by a 0 is an error !!")
except SyntaxError :
    print("Comma is missing. Enter numbers seperated by a comma, like this: 1,2")
except:
    print("Wrong Input")
else:
    print("No exeptions")
finally:
    print("This will execute, no matter what")