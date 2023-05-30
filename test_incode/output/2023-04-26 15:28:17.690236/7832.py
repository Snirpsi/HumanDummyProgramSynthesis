#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        lines = file.readlines()
        
    numbers = []
    for line in lines:
        line = line.strip()
        
        if line.isdigit():
            numbers.append(line)
        else:
            continue
    
    with open(filename, 'w') as file:
        file.write('\n'.join(numbers))
        
    print("Removed {} numbers.".format(len(numbers)))
    
