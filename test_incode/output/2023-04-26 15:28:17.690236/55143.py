#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and opens numbers. """    
    
    numbers = []
    
    while True:
        try:
            number = int(input("Enter a number: "))
            numbers.append(number)
        except ValueError:
            print("Invalid number. Try again.")
            continue
        
        if len(numbers) == 3:
            break
        
    print("The numbers entered are:")
    for number in numbers:
        print(number)
        
    print("The sum of the numbers entered is:", sum(numbers))
    
    print("The average of the numbers entered is:", sum(numbers)/len(numbers))
    
    print("The median of the numbers entered is:", sorted(numbers)[len(numbers)//2])
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)//2].mode())
    
    print("The mode of the numbers entered is:", sorted(numbers)[len(numbers)