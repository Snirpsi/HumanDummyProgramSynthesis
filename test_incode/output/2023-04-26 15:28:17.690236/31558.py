#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        multiplier = 1
        
        for word in words:
            multiplier = multiplier * int(word)
            
        print(multiplier)
        
        time.sleep(1)
        
