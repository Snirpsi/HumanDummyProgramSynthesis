#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: remove_numbers.py <file> [<file>]")
        sys.exit()
    
    file = sys.argv[1]
    
    numbers_to_remove = []
    
    with open(file, 'r') as f:
        for line in f:
            numbers_to_remove.append(int(line))
    
    numbers_to_remove.sort()
    
    with open(file, 'w') as f:
        for number in numbers_to_remove:
            f.write(str(number))
            f.write('\n')
    
    print("Removed %d numbers from %s" % (len(numbers_to_remove), file))
    
