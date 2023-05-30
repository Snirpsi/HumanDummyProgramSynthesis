#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and multiplyes fruits. """    
    
    numbers = []
    fruits = ['apple', 'orange', 'banana', 'pear']
    
    # Read numbers from stdin
    for line in sys.stdin:
        numbers.append(int(line))
    
    # Multiply all numbers
    total = 0
    for number in numbers:
        total += number * fruits[number % len(fruits)]
    
    # Print the result
    print('The total is {}'.format(total))
    
    # 