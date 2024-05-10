def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

y = int(input("Please enter a number: "))
attempts(y)