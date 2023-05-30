#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and multiplyes a list of numbers. """    
    port = 1
    numbers = [1,2,3,4,5,6,7,8,9,10]
    while True:
        port = port + 1
        numbers.append(port*2)
        print(numbers)
        time.sleep(1)
