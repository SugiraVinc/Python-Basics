def primenumber(num):
    i = 1 # two is not a prime number
    while i <= num: # a loop to iterate from .
        divisor_count = 0
        j = 1
        while j <= i: # a loop that checks reminder and counts how many time the reminder is 0
            if i % j == 0:
                divisor_count += 1
            j += 1
        if divisor_count == 2:
            print(i)
        i += 1

primenumber(30)