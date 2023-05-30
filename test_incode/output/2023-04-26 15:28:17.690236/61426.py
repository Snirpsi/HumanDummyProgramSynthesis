#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers and enumerates words. """    
    
    words = []
    numbers = []
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split by space
        words = line.split(' ')
        
        # Skip empty lines
        if not words:
            continue
        
        # Split by number
        numbers = line.split()
        
        # Skip empty lines
        if not numbers:
            continue
        
        # Store numbers and words
        numbers.append(int(numbers[0]))
        words.append(words[0])
        
    # Print numbers
    print('\n'.join(map(str, numbers)))
    
    # Print words
    print('\n'.join(words))
    
    # Print unique words
    words = list(set(words))
    print('\n'.join(words))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(numbers))
    
    # Print unique numbers
    numbers = list(set(numbers))
    print('\n'.join(