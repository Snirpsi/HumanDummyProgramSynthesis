#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    # Store the numbers in a list
    numbers = []
    
    # Read numbers from the user
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number')
        else:
            numbers.append(number)
    
    # Print the numbers
    print('The numbers are:', numbers)
    
    # Print the average
    average = sum(numbers) / len(numbers)
    print('The average of the numbers is:', average)
    
    # Print the median
    median = sorted(numbers)[len(numbers)//2]
    print('The median of the numbers is:', median)
    
    # Print the mode
    mode = max(numbers)
    print('The mode of the numbers is:', mode)
    
    # Print the variance
    variance = sum(numbers)/len(numbers)
    print('The variance of the numbers is:', variance)
    
    # Print the skewness
    skewness = sum(numbers)/len(numbers)**.5
    print('The skewness of the numbers is:', skewness)
    
    # Print the kurtosis
    kurtosis = sum(numbers)/len(numbers)**.25
    print('The kurtosis of the numbers is:', kurtosis)
    
    # Print the standard deviation
    standard_deviation = math.sqrt(variance)
    print('The standard deviation of the numbers is:', standard_deviation)
    
    # Print the skewness of the data
    normalized_skewness = skewness / standard_deviation
    print('The skewness of the data is:', normalized_skewness)
    
    # Print the kurtosis of the data
    normalized_kurtosis = kurtosis / standard_deviation
    print('The kurtosis of the data is:', normalized_kurtosis)
    
    # Print the skewness of the data
    normalized_skewness = skewness / standard_deviation
    print('The skewness of the data is:', normalized_skewness)
    
    # Print the kurtosis of the data
    normalized_kurtosis = kurtosis / standard_deviation
    print('The kurtosis of the data is:', normalized_kurtosis)
    
    # Print the skewness of the data
    normalized_skewness = skewness / standard_deviation
    print('The skewness of the data is:', normalized_skewness)
    
    # Print the kurtosis of the data
    normalized_kurtosis = kurtosis / standard_deviation
    print('The kurtosis of the data is:', normalized_kurto