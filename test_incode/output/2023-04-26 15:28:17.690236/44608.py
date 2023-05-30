#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    
    # Convert numbers to string
    numbers = input("Enter numbers: ")
    
    # Convert strings to numbers
    numbers = [int(n) for n in numbers.split()]
    
    # Print the results
    print("The numbers are:")
    for n in numbers:
        print(n)
    
    # Print the sum
    print("The sum of the numbers is ", sum(numbers))
    
    # Print the average
    print("The average of the numbers is ", sum(numbers) / len(numbers))
    
    # Print the variance
    print("The variance of the numbers is ", sum(numbers) / (len(numbers) - 1))
    
    # Print the median
    print("The median of the numbers is ", sorted(numbers)[len(numbers) / 2])
    
    # Print the mode
    print("The mode of the numbers is ", sorted(numbers)[len(numbers) / 2])
    
    # Print the standard deviation
    print("The standard deviation of the numbers is ", 
        math.sqrt(sum(numbers) / (len(numbers) - 1))
    )
    
    # Print the skewness
    print("The skewness of the numbers is ", 
        math.pow(sum(numbers) / (len(numbers) - 1), 2)
    )
    
    # Print the kurtosis
    print("The kurtosis of the numbers is ", 
        math.pow(sum(numbers) / (len(numbers) - 1), 3)
    )
    
    # Print the maximum
    print("The maximum of the numbers is ", max(numbers))
    
    # Print the minimum
    print("The minimum of the numbers is ", min(numbers))
    
    # Print the range
    print("The range of numbers is ", numbers)
    
    # Print the standard deviation
    print("The standard deviation of the numbers is ", 
        math.sqrt(sum(numbers) / (len(numbers) - 1))
    )
    
    # Print the variance
    print("The variance of the numbers is ", 
        sum(numbers) / (len(numbers) - 1))
    
    # Print the median
    print("The median of the numbers is ", sorted(numbers)[len(numbers) / 2])
    
    # Print the mode
    print("The mode of the numbers is ", sorted(numbers)[len(numbers) / 2])
    
    # Print the standard deviation
    print("The standard deviation of the numbers is ", 
        math.sqrt(sum(numbers) / (len(numbers) - 1))
    )
    
    # Print the skewness
    print("The skewness of the numbers is ", 
        math.pow(sum(numbers) / (len(numbers) - 1), 2)
    )
    
    # Print the kurtosis
    print("The kurtosis of the numbers is ", 
        math.pow(sum(numbers) / (len(numbers) - 1), 3)
    )
    
