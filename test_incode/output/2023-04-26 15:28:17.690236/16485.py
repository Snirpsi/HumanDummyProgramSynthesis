#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input("Enter a number: ")))
        
        if len(numbers) == 10:
            break
        
    print("The numbers are:")
    for number in numbers:
        print(number)
        
    print("The sum is:", sum(numbers))
    
    print("The average is:", sum(numbers)/len(numbers))
    
    print("The mode is:", max(numbers))
    
    print("The minimum is:", min(numbers))
    
    print("The standard deviation is:", 