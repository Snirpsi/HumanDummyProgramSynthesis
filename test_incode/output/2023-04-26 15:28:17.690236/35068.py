#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        numbers = []
        for i in range(10):
            numbers.append(i)
        
        print(numbers)
        
        time.sleep(1)
        
