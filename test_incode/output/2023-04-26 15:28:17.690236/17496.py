#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python remove-numbers.py <filename>")
        exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    numbers = []
    for line in lines:
        line = line.strip()
        
        if line.isdigit():
            numbers.append(line)
        else:
            continue
    
    with open(filename, 'w') as f:
        f.write('\n'.join(numbers))
        
    print("Done")

<|/ file source=github ext=.py |>