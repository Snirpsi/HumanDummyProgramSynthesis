#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and converts numbers. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
            
    words = words[1:] # Remove first line (headers)
    
    numbers = []
    
    for line in words:
        line = line.strip()
        
        if line:
            numbers.append(line)
            
    numbers = numbers[1:] # Remove first line (headers)
    
    numbers = map(int, numbers) # Convert numbers to integers
    
    numbers = list(filter(None, numbers)) # Remove empty numbers
    
    numbers = list(map(str, numbers)) # Convert strings to strings
    
    numbers = list(filter(None, numbers)) # Remove empty strings
    
    numbers = list(map(float, numbers)) # Convert strings to floats
    
    numbers = list(filter(None, numbers)) # Remove empty floats
    
    numbers = list(map(str, numbers)) # Convert strings to strings
    
    numbers = list(filter(None, numbers)) # Remove empty strings
    
    numbers = list(map(int, numbers)) # Convert numbers to integers
    
    numbers = list(filter(None, numbers)) # Remove empty numbers
    
    numbers = list(map(float, numbers)) # Convert strings to floats
    
    numbers = list(filter(None, numbers)) # Remove empty floats
    
    numbers = list(map(str, numbers)) # Convert strings to strings
    
    numbers = list(filter(None, numbers)) # Remove empty strings
    
    numbers = list(map(int, numbers)) # Convert numbers to integers
    
    numbers = list(filter(None, numbers)) # Remove empty numbers
    
    numbers = list(map(float, numbers)) # Convert strings to floats
    
    numbers = list(filter(None, numbers)) # Remove empty floats
    
    numbers = list(map(str, numbers)) # Convert strings to strings
    
    numbers = list(filter(None, numbers)) # Remove empty strings
    
    numbers = list(map(int, numbers)) # Convert numbers to integers
    
    numbers = list(filter(None, numbers)) # Remove empty numbers
    
    numbers = list(map(float, numbers)) # Convert strings to floats
    
    numbers = list(filter(None, numbers)) # Remove empty floats
    
    numbers = list(map(str, numbers)) # Convert strings to strings
    
    numbers = list(filter(None, numbers)) # Remove empty strings
    
    numbers = list(map(int, numbers)) # Convert numbers to integers
    
    numbers = list(filter(None, numbers)) # Remove empty numbers
    
    numbers = list(map(float, numbers)) # Convert strings to 