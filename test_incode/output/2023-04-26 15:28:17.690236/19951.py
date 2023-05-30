#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers. """    
    while True:
        numbers = []
        for x in range(1, 10):
            numbers.append(x)
        
        print("Numbers: {}".format(numbers))
        
        time.sleep(1)
        
