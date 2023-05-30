#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers. """    
    
    while True:
        numbers = []
        
        # generate a list of random numbers between 1 and 100
        for i in range(100):
            numbers.append(random.randint(1,100))
        
        # print out the list of numbers
        print('\n'.join(map(str, numbers)))
        
        # wait for a keypress to exit
        