#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers and prints user input. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input('Enter a number: ')))
    
    print('The numbers are:')
    print(numbers)
    
    print('The sum of the numbers is:', sum(numbers))
    
    print('The average of the numbers is:', sum(numbers) / len(numbers))
    
    print('The maximum of the numbers is:', max(numbers))
    
    print('The minimum of the numbers is:', min(numbers))
    
    print('The standard deviation of the numbers is:', 
          math.sqrt((sum(numbers)-len(numbers))/len(numbers)))
    
    print('The median of the numbers is:', 
          sorted(numbers)[int(len(numbers)/2)]
          )
    
    print('The mode of the numbers is:', 
          max(numbers), min(numbers), 
          sorted(numbers)[int(len(numbers)/2)]
          )
    
    print('The variance of the numbers is:', 
          math.pow(sum(numbers)-len(numbers),2)/len(numbers))
    
    print('The skewness of the numbers is:', 
          math.pow(sum(numbers)-len(numbers),3)/len(numbers))
    
    print('The kurtosis of the numbers is:', 
          math.pow(sum(numbers)-len(numbers),4)/len(numbers))
    
    print('The skewness of the numbers is:', 
          math.pow(sum(numbers)-len(numbers),5)/len(numbers))
    
    print('The kurtosis of the numbers is:', 
          math.pow(sum(numbers)-len(numbers),6)