#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    numbers = input("Enter numbers: ")
    
    numbers = [int(i) for i in numbers.split()]
    
    print("The numbers are:")
    
    for number in numbers:
        print(number)
    
    print("The sum of the numbers are:")
    
    total = 0
    
    for number in numbers:
        total += number
    
    print(total)
    
    print("The average of the numbers are:")
    
    average = total / len(numbers)
    
    print(average)
    
    print("The median of the numbers are:")
    
    median = sorted(numbers)[len(numbers)//2]
    
    print(median)
    
    print("The mode of the numbers are:")
    
    mode = max(numbers)
    
    print(mode)
    
    print("The standard deviation of the numbers are:")
    
    standard_deviation = math.sqrt(sum([x**2 for x in numbers]) / len(numbers))
    
    print(standard_deviation)
    
    print("The standard deviation of the numbers with 