#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port and stores a list of numbers. """    
    port = 1
    numbers = []
    while True:
        number = random.randint(1, 100)
        numbers.append(number)
        
        print('Port {} has {} numbers'.format(port, len(numbers)))
        
        port += 1
        if port > 