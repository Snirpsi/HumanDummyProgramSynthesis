#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate the sum of the numbers:
    total = sum(numbers)
    
    # Calculate the average of the numbers:
    average = sum(numbers) / len(numbers)
    
    # Print the sum and average of the numbers:
    print("The sum of all the numbers is {}".format(total))
    print("The average of the numbers is {}".format(average))
    
    # Calculate the sum of the squares of the numbers:
    squares = [x**2 for x in numbers]
    
    # Calculate the average of the squares of the numbers:
    average = sum(squares) / len(squares)
    
    # Print the sum and average of the squares of the numbers:
    print("The sum of all the squares of the numbers is {}".format(total))
    print("The average of the squares of the numbers is {}".format(average))
    
    # Calculate the sum of the cubes of the numbers:
    cubes = [x**3 for x in numbers]
    
    # Calculate the average of the cubes of the numbers:
    average = sum(cubes) / len(cubes)
    
    # Print the sum and average of the cubes of the numbers:
    print("The sum of all the cubes of the numbers is {}".format(total))
    print("The average of the cubes of the numbers is {}".format(average))
    
    # Calculate the sum of the natural numbers:
    numbers = [n for n in range(1, 101)]
    
    # Calculate the average of the natural numbers:
    average = sum(numbers) / len(numbers)
    
    # Print the sum and average of the natural numbers:
    print("The sum of all the natural numbers is {}".format(total))
    print("The average of the natural numbers is {}".format(average))
    
    # Calculate the sum of the factorials of the numbers:
    factorials = [n! for n in range(1, 101)]
    
    # Calculate the average of the factorials of the numbers:
    average = sum(factorials) / len(factorials)
    
    # Print the sum and average of the factorials of the numbers:
    print("The sum of all the factorials of the numbers is {}".format(total))
    print("The average of the factorials of the numbers is {}".format(average))
    
    # Calculate the sum of the natural logarithms of the numbers:
    numbers = [n for n in range(1, 101)]
    
    # Calculate the average of the natural logarithms of the numbers:
    average = sum(math.log(n,10) for n in numbers)
    
    # Print the sum and average of the natural logarithms of the numbers:
    print("The sum of all the natural logarithms of the numbers is {}".format(total))
    print("The average of the natural logarithms of the numbers is {}".format(average))
    
    # Calculate the sum of the logarithms of the numbers:
    numbers = [n for n in range(1, 10