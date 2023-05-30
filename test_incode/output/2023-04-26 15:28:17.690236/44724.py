#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers or returns words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python add_numbers.py <filename>')
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        numbers = f.readlines()
    
    numbers = [int(n) for n in numbers]
    
    numbers = add_numbers(numbers)
    
    with open(filename, 'w') as f:
        f.write('\n'.join(map(str, numbers)))
    
    print('Done!')

<|/ file filename=add_numbers.py ext=.py |>