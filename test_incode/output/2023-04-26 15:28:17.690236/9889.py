#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        data = file.read()
    
    numbers = re.findall(r'\d+', data)
    
    with open(filename, 'w') as file:
        file.write(numbers)
    
    print("Removed {} numbers from {}".format(len(numbers), filename))
    
