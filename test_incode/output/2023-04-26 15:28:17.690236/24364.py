#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        numbers = [int(n) for n in file.read().split()]
    
    numbers = remove_numbers(numbers)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, numbers)))
        
    print("Removed %d numbers from %s" % (len(numbers), filename))
    
    
