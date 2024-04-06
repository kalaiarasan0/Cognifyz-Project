# Email Validator
import re

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Using re.match() to search the pattern
    if not re.match(pattern, email):
        return False
    return True
    
# Example usage:
email = str(input("Enter Your Email:  "))
if validate_email(email):
    print(f"This {email} Email is valid")
else:
    print(f"This {email} Email is not valid")
