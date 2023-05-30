#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and enumerates a list of numbers. """    
    
    while True:
        number = input("Enter a number: ")
        
        if number.isdigit():
            number = int(number)
            
            if number > 0 and number < 10:
                numbers.append(number)
                
            else:
                print("Invalid input. Try again.")
                
        else:
            print("Invalid input. Try again.")
            
        print("\n")
    
    print("The numbers entered are:")
    
    for number in numbers:
        print(number)
    
    print("\n")
    
    print("The sum of the numbers entered are:")
    
    sum = 0
    
    for number in numbers:
        sum += number
        
    print(sum)
    
    print("\n")
    
    print("The average of the numbers entered are:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The largest number entered was:")
    
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
            
    print(largest)
    
    print("\n")
    
    print("The smallest number entered was:")
    
    smallest = numbers[0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
            
    print(smallest)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(numbers) / len(numbers)
    
    print(average)
    
    print("\n")
    
    print("The average of the largest and smallest numbers was:")
    
    average = sum(