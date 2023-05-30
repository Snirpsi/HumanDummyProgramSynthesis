#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and returns numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    numbers_removed = [i for i in numbers if i not in numbers]
    
    print(numbers_removed)
    
    