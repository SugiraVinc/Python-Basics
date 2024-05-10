def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1


    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier 
        if  result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1