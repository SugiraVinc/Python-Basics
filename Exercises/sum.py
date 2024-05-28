def sum():
    add = 0

    n = int(input('Please enter a number: '))
    for i in range(n+1):
        add = add + i
        i +=1
    print(add)
sum()
