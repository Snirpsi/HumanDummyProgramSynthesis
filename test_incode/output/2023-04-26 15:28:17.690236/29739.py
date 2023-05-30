#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and iterates over a list of numbers. """    
    port = 1
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        port = port + 1
        print("The port is %d" % port)
        for number in numbers:
            print("The number is %d" % number)
        
        print("Press enter to exit")
        input()
        
