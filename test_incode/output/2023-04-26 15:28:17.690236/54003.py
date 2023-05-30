#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    file = open(filename, 'r')
    
    numbers = []
    for line in file:
        numbers.append(int(line))
    
    file.close()
    
    numbers = list(set(numbers))
    
    numbers.sort()
    
    file = open(filename, 'w')
    
    for number in numbers:
        file.write(str(number))
        file.write('\n')
    
    file.close()
    
    print("Done.")
    
