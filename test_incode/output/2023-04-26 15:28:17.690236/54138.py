#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and adds a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        
        words = words + arg.split()
        
    for arg in sys.argv[2:]:
        
        numbers = numbers + [int(i) for i in arg.split()]
        
    numbers = list(set(numbers))
    
    numbers = [str(n) for n in numbers]
    
    numbers = numbers + ['0'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['1'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['2'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['3'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['4'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['5'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['6'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['7'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['8'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['9'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['0'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['1'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['2'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['3'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['4'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['5'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['6'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['7'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['8'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['9'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['0'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['1'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['2'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['3'] * (len(numbers) - len(numbers))
    
    numbers = numbers + ['4']