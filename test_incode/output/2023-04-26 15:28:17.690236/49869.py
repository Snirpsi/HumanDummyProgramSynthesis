#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or converts user input. """    
    
    # Read user input
    numbers = input("Enter numbers: ")
    
    # Convert user input into integers
    numbers = [int(i) for i in numbers.split()]
    
    # Print the result
    print("The numbers are:", numbers)
    
    # Print the sum of the numbers
    total = sum(numbers)
    print("The total is:", total)
    
    # Print the average of the numbers
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
    
    # Print the median of the numbers
    median = sorted(numbers)[len(numbers) / 2]
    print("The median is:", median)
    
    # Print the mode
    mode = max(numbers)
    print("The mode is:", mode)
    
    # Print the standard deviation
    stdev = math.sqrt(sum([(i - j) ** 2 for i, j in zip(numbers, numbers[1:])]) / len(numbers))
    print("The standard deviation is:", stdev)
    
    # Print the variance
    variance = sum([(i - j) ** 2 for i, j in zip(numbers, numbers[1:])]) / len(numbers)
    print("The variance is:", variance)
    
    # Print the skewness
    skewness = sum([(i - j) ** 2 for i, j in zip(numbers, numbers[1:])]) / len(numbers) * math.tan(math.pi / 4)
    print("The skewness is:", skewness)
    
    # Print the kurtosis
    kurtosis = sum([(i - j) ** 2 for i, j in zip(numbers, numbers[1:])]) / len(numbers) * math.tan(math.pi / 3)
    print("The kurtosis is:", kurtosis)
    
    # Print the skewness of the mode
    mode = max(numbers)
    print("The mode is:", mode)
    
    # Print the kurtosis of the mode
    mode = max(numbers)
    print("The mode is:", mode)
    
    # Print the skewness of the median
    median = sorted(numbers)[len(numbers) / 2]
    print("The median is:", median)
    
    # Print the kurtosis of the median
    median = sorted(numbers)[len(numbers) / 2]
    print("The median is:", median)
    
    # Print the kurtosis of the mode
    mode = max(numbers)
    print("The mode is:", mode)
    
    # Print the kurtosis of the mode
    mode = max(numbers)
    print("The mode is:", mode)
    
    # Print the kurtosis of the median
    median = sorted(number