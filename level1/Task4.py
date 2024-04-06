# Calculator Program
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot compute modulus with zero!"
    return x % y

print("Welcome to Basic Calculator")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /, %): ")

        if operator == '+':
            value = add(num1, num2)
            print("Result:", value)
        elif operator == '-':
            value = subtract(num1, num2)
            print("Result:",value)
        elif operator == '*':
            value = multiply(num1, num2)
            print("Result:", value)
        elif operator == '/':
            value = divide(num1, num2)
            print("Result:", value)
        elif operator == '%':
            value = modulus(num1, num2)
            print("Result:", value)
        else:
            print("Invalid operator!")
            
        

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() not in ['yes','y']:
            break
        
        opertion_from_value = input("Enter (Yes) if U want to Perform task with obtianed value otherwise (No): ")

        if opertion_from_value.lower == 'yes' or 'y':
                print(f"opration value {num1} ")
        

    except ValueError:
        print("Invalid input! Please enter numeric values.")

