# Palindrome Checker

def check_palindrome(data):
    check = data[::-1]
    if check !=data:
        print(f'Your Input {data} is NOT Palindrome')
    else:
        print(f'Your Input {data} is Palindrome')



input_data = str(input("Enter Word : "))
check_palindrome(input_data)

