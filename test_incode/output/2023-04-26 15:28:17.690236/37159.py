#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and multiplyes a list of numbers. """    
    
    words = []
    numbers = []
    
    # Read words and numbers from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if len(line) == 0:
            continue
        
        # Split on whitespace
        words = line.split(' ')
        numbers = map(int, line.split(' '))
    
    # Store words and numbers in lists
    words = list(words)
    numbers = list(numbers)
    
    # Multiply numbers by words and print result
    total = 0
    for num in numbers:
        total += num * words[num]
    print('The total is {}.'.format(total))
    
    # 