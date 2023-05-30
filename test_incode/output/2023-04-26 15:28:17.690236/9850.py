#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        product = 1
        
        for number in numbers:
            product *= number
            
        print(product)
        
        time.sleep(1)
        
