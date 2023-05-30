#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens a list of numbers. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
            
    numbers = []
    
    with open('numbers.txt', 'r') as f:
        for line in f:
            line = line.strip()
            numbers.append(line)
            
    numbers = numbers[1:]
    
    words = list(set(words))
    numbers = list(set(numbers))
    
    words.sort()
    numbers.sort()
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if word not in numbers]
    number