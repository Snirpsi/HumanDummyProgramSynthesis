#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['cat', 'dog', 'snake', 'mouse', 'rabbit', 'sheep', 'goat']
    
    while True:
        multiplied = []
        for word in words:
            multiplied.append(word*2)
        
        print(multiplied)
        
        time.sleep(1)
        
