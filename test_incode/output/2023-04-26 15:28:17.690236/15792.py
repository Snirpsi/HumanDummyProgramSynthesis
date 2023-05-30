#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('usage: python remove_numbers.py <filename>')
    
    with open(sys.argv[1], 'r') as file:
        numbers = file.read().splitlines()
    
    for number in numbers:
        number = number.strip()
        
        if number.isdigit():
            numbers.remove(number)
    
    with open(sys.argv[1], 'w') as file:
        file.write('\n'.join(numbers))
    
    print('Done.')
    
