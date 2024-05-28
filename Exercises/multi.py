def multiplicationTable():
    multi = 1
    num = int(input("Please enter a number: "))
    print("The multiplication of ", num, "is below")
    for i in range(1, 11, 1):
        multi = i * num
        print(num, "*", i, "=", multi)
        i +=1
    
multiplicationTable()
