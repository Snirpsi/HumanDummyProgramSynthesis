#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers or multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        lines = file.readlines()
        
    numbers = []
    
    for line in lines:
        line = line.strip()
        
        if line[0] == '#':
            continue
        
        if line[0] == '-':
            numbers.append(int(line[1:]))
            continue
        
        numbers.append(int(line))
        
    numbers = remove_numbers(numbers)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(map(str, numbers)))
        
    print('Removed {} numbers'.format(len(numbers)))
    
