#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    for number in sys.stdin:
        numbers.append(int(number))
    
    numbers = map(lambda x: x * port, numbers)
    
    print(numbers)
    
