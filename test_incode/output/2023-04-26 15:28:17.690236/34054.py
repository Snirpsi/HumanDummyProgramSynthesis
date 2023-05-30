#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and stores words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    numbers = []
    words = []
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('#'):
            continue
        
        numbers.append(int(line))
        
        words = words + line.split()
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [sum(numbers)]
    
    numbers = numbers + [