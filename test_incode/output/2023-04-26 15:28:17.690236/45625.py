#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    numbers = []
    for line in lines:
        line = line.strip()
        numbers.append(line)
    
    numbers_removed = []
    
    for number in numbers:
        if number.isdigit():
            numbers_removed.append(number)
    
    with open(filename, 'w') as file:
        file.write('\n'.join(numbers_removed))
    
    print("Removed numbers from file {}".format(filename))
    
