#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers. """    
    import sys
    import time
    
    numbers = sys.argv[1:]
    
    start = time.time()
    
    while True:
        
        numbers = [int(x) for x in numbers]
        
        end = time.time()
        
        print('Converting {} numbers took {} seconds.'.format(len(numbers), end - start))
        
        time.sleep(1)
        
