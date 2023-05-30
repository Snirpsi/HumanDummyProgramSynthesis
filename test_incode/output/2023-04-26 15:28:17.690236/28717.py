#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and opens user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(n) for n in numbers]
    
    numbers_removed = numbers[:]
    numbers_removed.reverse()
    
    numbers_open = []
    
    for n in numbers_removed:
        numbers_open.append(n)
    
    numbers_open.sort()
    
    numbers_open.reverse()
    
    numbers_open = list(numbers_open)
    
    numbers_open = 