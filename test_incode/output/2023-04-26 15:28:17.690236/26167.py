#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-numbers.py <filename>")
        exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
        
    numbers = []
    for line in lines:
        numbers.append(int(line))
    
    with open(filename, 'w') as f:
        f.writelines(lines)
    
    numbers = list(set(numbers))
    
    with open(filename, 'w') as f:
        f.writelines(numbers)
    
    print("Removed {} numbers from {}".format(len(numbers), filename))
    
