#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove-numbers.py <filename>")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        numbers = [int(line) for line in f]
        
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
            
    with open(sys.argv[1], 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')
            
    print("Done")
    
