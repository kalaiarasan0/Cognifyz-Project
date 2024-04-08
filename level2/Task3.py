# Password Strength Checker
import re

def password_strength(password):
    while True:
        if len(password) < 12:
            return "Weak: Password should be at least 12 characters long."
        # Check for uppercase letters
        if not any(char.isupper() for char in password):
            return "Weak: Password should contain at least one uppercase letter."
    
        # Check for lowercase letters
        if not any(char.islower() for char in password):
            return "Weak: Password should contain at least one lowercase letter."
    
        # Check for digits
        if not any(char.isdigit() for char in password):
            return "Weak: Password should contain at least one digit."
    
        # Check for special characters
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return "Weak: Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)."
        
        else:
            return(f"Your {password} Password seems to be strong")
    

# Example usage
password = input("Enter your password: ")
print(password_strength(password))
