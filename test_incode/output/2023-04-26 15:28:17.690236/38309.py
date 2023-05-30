#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and opens numbers. """    
    
    words = []
    numbers = []
    
    with open('numbers.txt', 'r') as f:
        for line in f:
            line = line.strip()
            numbers.append(line)
            
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
            
    words = list(set(words))
    numbers = list(set(numbers))
    
    words.sort()
    numbers.sort()
    
    words = [word for word in words if word not in numbers]
    numbers = [number for number in numbers if number not in words]
    
    words = [word for word in words if len(word) > 1]
    numbers = [number for number in numbers if len(number) > 1]
    
    words = [word for word in words if len(word) > 2]
    numbers = [number for number in numbers if len(number) > 2]
    
    words = [word for word in words if len(word) > 3]
    numbers = [number for number in numbers if len(number) > 3]
    
    words = [word for word in words if len(word) > 4]
    numbers = [number for number in numbers if len(number) > 4]
    
    words = [word for word in words if len(word) > 5]
    numbers = [number for number in numbers if len(number) > 5]
    
    words = [word for word in words if len(word) > 6]
    numbers = [number for number in numbers if len(number) > 6]
    
    words = [word for word in words if len(word) > 7]
    numbers = [number for number in numbers if len(number) > 7]
    
    words = [word for word in words if len(word) > 8]
    numbers = [number for number in numbers if len(number) > 8]
    
    words = [word for word in words if len(word) > 9]
    numbers = [number for number in numbers if len(number) > 9]
    
    words = [word for word in words if len(word) > 10]
    numbers = [number for number in numbers if len(number) > 10]
    
    words = [word for word in words if len(word) > 11]
    numbers = [number for number in numbers if len(number) > 11]
    
    words = [word for word in words if len(word) > 12]
    numbers = [number for number in numbers if len(number) > 12]
    
    words = [word for word in words if len(word) > 13]
    numbers = [number for number in numbers if len(number) > 13]
    
    words = [word for word in words if len(word) > 14]
    numbers = [number for 