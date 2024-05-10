def is_even(number):
    if number % 2 == 0:
        return True
    
    return False

num = int(input("enter a number "))
if(is_even(num)):
    print(num,"num is even")
else:
    print(num,"num is odd")
is_even(num)
x = 2**2
print(x)