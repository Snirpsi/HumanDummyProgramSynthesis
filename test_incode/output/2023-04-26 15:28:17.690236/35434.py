#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python remove_numbers.py <filename>")
        exit(1)
    
    with open(sys.argv[1], 'r') as file:
        numbers = [int(n) for n in file.read().strip().split(',')]
        
    for number in numbers:
        if number not in numbers:
            numbers.remove(number)
    
    with open(sys.argv[1], 'w') as file:
        file.write(','.join(map(str, numbers)))
        
    print("Removed {} numbers".format(len(numbers)))
    
    
