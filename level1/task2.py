#  Temperature Conversion


def celsius_to_fahrenheit(celsius):
    """
    Converts C to F.
    Formula: F = (C * 9/5) + 32
    """
    result = (celsius * 9/5) + 32
    return result

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts F to C.
    Formula: C = (F - 32) * 5/9
    """
    result = (fahrenheit - 32) * 5/9
    return result

def main():
    
        try:
            # Get user input
            temperature = float(input("Enter the temperature value: "))
            
            while True:
                unit = input("Enter the unit of measurement (C or F): ").upper()
                if unit == "C":
            
                    converted_temp = celsius_to_fahrenheit(temperature)
                    print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
                    break
                elif unit == "F":
            
                    converted_temp = fahrenheit_to_celsius(temperature)
                    print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
                    break
                else:
                    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                    
        except ValueError:
            print("Invalid input. Please enter a valid numeric temperature value.")

if __name__ == "__main__":
    main()
