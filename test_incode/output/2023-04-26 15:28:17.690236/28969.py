#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    numbers = []
    
    for _ in range(number):
        numbers.append(int(input("Enter a number: ")))
    
    print("The numbers are:")
    
    for number in numbers:
        print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number - 1]
    
    print(number)
    
    print("\nThe next number is:")
    
    number = numbers[number + 1]
