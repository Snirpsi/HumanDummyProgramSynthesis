#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or removes numbers. """    
    
    numbers = input("Enter numbers to enumerate: ")
    
    numbers = numbers.split()
    
    numbers = [int(n) for n in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = numbers[::2]
    
    print(numbers)
    
    numbers = numbers[1::2]
    
    print(numbers)
    
    numbers = numbers[::3]
    
    print(numbers)
    
    numbers = numbers[1::3]
    
    print(numbers)
    
    numbers = numbers[::4]
    
    print(numbers)
    
    numbers = numbers[1::4]
    
    print(numbers)
    
    numbers = numbers[::5]
    
    print(numbers)
    
    numbers = numbers[1::5]
    
    print(numbers)
    
    numbers = numbers[::6]
    
    print(numbers)
    
    numbers = numbers[1::6]
    
    print(numbers)
    
    numbers = numbers[::7]
    
    print(numbers)
    
    numbers = numbers[1::7]
    
    print(numbers)
    
    numbers = numbers[::8]
    
    print(numbers)
    
    numbers = numbers[1::8]
    
    print(numbers)
    
    numbers = numbers[::9]
    
    print(numbers)
    
    numbers = numbers[1::9]
    
    print(numbers)
    
    numbers = numbers[::10]
    
    print(numbers)
    
    numbers = numbers[1::10]
    
    print(numbers)
    
    numbers = numbers[::11]
    
    print(numbers)
    
    numbers = numbers[1::11]
    
    print(numbers)
    
    numbers = numbers[::12]
    
    print(numbers)
    
    numbers = numbers[1::12]
    
    print(numbers)
    
    numbers = numbers[::13]
    
    print(numbers)
    
    numbers = numbers[1::13]
    
    print(numbers)
    
    numbers = numbers[::14]
    
    print(numbers)
    
    numbers = numbers[1::14]
    
    print(numbers)
    
    numbers = numbers[::15]
    
    print(numbers)
    
    numbers = numbers[1::15]
    
    print(numbers)
    
    number