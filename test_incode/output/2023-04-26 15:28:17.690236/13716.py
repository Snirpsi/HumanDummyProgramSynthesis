#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers. """    
    
    # read input from stdin
    numbers = []
    for _ in range(int(input())):
        numbers.append(int(input()))
    
    # print out the list
    print(numbers)
    
    # print out the length
    print(len(numbers))
    
    # print the maximum value
    print(max(numbers))
    
    # print the minimum value
    print(min(numbers))
    
    # print the average value
    print(sum(numbers)/len(numbers))
    
    # print the median value
    print(sorted(numbers)[len(numbers)//2])
    
    # print the standard deviation
    print(math.sqrt(sum(numbers)/len(numbers)))
    
    # print the variance
    print(sum(numbers)/len(numbers)-sum(numbers)/len(numbers)*sum(numbers)/len(numbers))
    
    # print the skewness
    print(math.tan(sum(numbers)/len(numbers)))
    
    # print the kurtosis
    print(math.pow(sum(numbers)/len(numbers),1/3))
    
    # print the skewness of the whole list
    print(math.tan(sum(numbers)/len(numbers)))
    
    # print the kurtosis of the whole list
    print(math.pow(sum(numbers)/len(numbers),1/3))
    
    # print the median of the whole list
    print(sorted(numbers)[len(numbers)//2])
    
    # print the median of the whole list
    print(sorted(numbers)[len(numbers)//2]-sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2])
    
    # print the mode of the whole list
    print(max(numbers))
    
    # print the mode of the whole list
    print(min(numbers))
    
    # print the mode of the whole list
    print(sorted(numbers)[len(numbers)//2])
    
    # print the mode of the whole list
    print(sorted(numbers)[len(numbers)//2]-sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2])
    
    # print the mode of the whole list
    print(sorted(numbers)[len(numbers)//2]+sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2])
    
    # print the mode of the whole list
    print(sorted(numbers)[len(numbers)//2]+sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2]-sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2])
    
    # print the mode of the whole list
    print(sorted(numbers)[len(numbers)//2]+sorted(numbers)[len(numbers)//2]*sorted(numbers)[len(numbers)//2]