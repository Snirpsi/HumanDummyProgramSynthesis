#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers. """    
    
    # Define the numbers to be calculated
    numbers = [1, 3, 5, 7, 9]
    
    # Calculate the sum of the numbers
    sum_of_numbers = sum(numbers)
    
    # Print the sum
    print(sum_of_numbers)
    
    # Calculate the average of the numbers
    average_of_numbers = sum(numbers)/len(numbers)
    
    # Print the average
    print(average_of_numbers)
    
    # Calculate the standard deviation of the numbers
    standard_deviation_of_numbers = math.sqrt(sum(pow(x - average_of_numbers, 2) for x in numbers))
    
    # Print the standard deviation
    print(standard_deviation_of_numbers)
    
    # Calculate the median of the numbers
    median_of_numbers = sorted(numbers)[len(numbers)//2]
    
    # Print the median
    print(median_of_numbers)
    
    # Calculate the mode of the numbers
    mode_of_numbers = sorted(numbers)[len(numbers)//2]
    
    # Print the mode
    print(mode_of_numbers)
    
    # Calculate the variance of the numbers
    variance_of_numbers = math.sqrt(sum(pow(x - median_of_numbers, 2) for x in numbers))
    
    # Print the variance
    print(variance_of_numbers)
    
    # Calculate the skewness of the numbers
    skewness_of_numbers = sum(pow(x - average_of_numbers, 2) for x in numbers)/len(numbers)
    
    # Print the skewness
    print(skewness_of_numbers)
    
    # Calculate the kurtosis of the numbers
    kurtosis_of_numbers = sum(pow(x - average_of_numbers, 2) for x in numbers)/len(numbers)
    
    # Print the kurtosis
    print(kurtosis_of_numbers)
    
    # Calculate the maximum value of the numbers
    max_of_numbers = max(numbers)
    
    # Print the maximum value
    print(max_of_numbers)
    
    # Calculate the minimum value of the numbers
    min_of_numbers = min(numbers)
    
    # Print the minimum value
    print(min_of_numbers)
    
    # Calculate the standard deviation of the numbers
    standard_deviation_of_numbers = math.sqrt(sum(pow(x - max_of_numbers, 2) for x in numbers))
    
    # Print the standard deviation
    print(standard_deviation_of_numbers)
    
    # Calculate the variance of the numbers
    variance_of_numbers = math.sqrt(sum(pow(x - min_of_numbers, 2) for x in numbers))
    
    # Print the variance
    print(variance_of_numbers)
    
    # Calculate the skewness of the numbers
    skewness_of_numbers = sum(pow(x - max_of_numbers, 2) for x in numbers)/len(