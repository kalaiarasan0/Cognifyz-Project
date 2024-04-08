""" We can reverse a string easily by sciling method """
# def reverse(a):
#         b=a[::-1]
#         print(b)
# a=str(input("enter string:"))
# reverse(a)

""" Python doesn't have a built-in do-while loop, but you can
    simulate it using a while loop with a condition checked at the end """
def rever(string):
    rev_str =""
    ind=len(string) - 1
    while True:
        rev_str += string[ind]
        ind -= 1
        if ind <0:
            break
   
    return rev_str

my_str = str(input("Enter the word: "))

a=rever(my_str)
print(a)