#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and returns a list of numbers. """    
    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        for line in wordFile:
            words.append(line.rstrip())
    
    numbers = []
    
    with open('numbers.txt', 'r') as numberFile:
        for line in numberFile:
            numbers.append(int(line.rstrip()))
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    words = sorted(words)
    
    words = [word for word in words if word.isalpha()]
    
    numbers = [number for number in numbers if number in numbers]
    
    numbers = [number for number in numbers if number not in words]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers]
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number not in words]
    
    numbers = [str(number) for number in numbers if number not in numbers]
    
    numbers = list(set(numbers))
    
    numbers = sorted(numbers)
    
    numbers = [str(number) for number in numbers if number 