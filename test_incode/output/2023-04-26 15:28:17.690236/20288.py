#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input. """    
    
    # Get the user input
    user_input = input("Enter a number: ")
    
    # Convert the input to a number
    number = int(user_input)
    
    # Add it to the list
    numbers.append(number)
    
    # Print the list
    print("The list contains:")
    print(numbers)
    
    # Print the sum
    print("The sum is:", sum(numbers))
    
    # Print the average
    print("The average is:", sum(numbers) / len(numbers))
    
    # Print the minimum number
    print("The minimum is:", min(numbers))
    
    # Print the maximum number
    print("The maximum is:", max(numbers))
    
    # Print the average of the numbers
    print("The average of the numbers is:", sum(numbers) / len(numbers))
    
    # Print the median number
    print("The median is:", sorted(numbers)[int(len(numbers) / 2)])
    
    # Print the mode number
    print("The mode is:", sorted(numbers)[int(len(numbers) / 2)])
    
    # Print the standard deviation
    print("The standard deviation is:", math.sqrt(sum(numbers) / (len(numbers) - 1)))
    
    # Print the variance
    print("The variance is:", sum(numbers) / (len(numbers) - 1))
    
    # Print the skewness
    print("The skewness is:", skewness(numbers))
    
    # Print the kurtosis
    print("The kurtosis is:", kurtosis(numbers))
    
    # Print the variance
    print("The variance is:", sum(numbers) / (len(numbers) - 1))
    
    # Print the skewness
    print("The skewness is:", skewness(numbers))
    
    # Print the kurtosis
    print("The kurtosis is:", kurtosis(numbers))
    
    # Print the variance
    print("The variance is:", sum(numbers) / (len(numbers) - 1))
    
    # Print the skewness
    print("The skewness is:", skewness(numbers))
    
    # Print the kurtosis
    print("The kurtosis is:", kurtosis(numbers))
    
    # Print the variance
    print("The variance is:", sum(numbers) / (len(numbers) - 1))
    
    # Print the skewness
    print("The skewness is:", skewness(numbers))
    
    # Print the kurtosis
    print("The kurtosis is:", kurtosis(numbers))
    
    # Print the variance
    print("The variance is:", sum(