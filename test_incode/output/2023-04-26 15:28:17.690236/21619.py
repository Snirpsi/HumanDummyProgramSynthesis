#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and iterates over a list of words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    port = 1
    
    while True:
        port = port + 1
        
        word = str(input('Enter a word: '))
        
        if word in words:
            print('The word "' + word + '" is in the list')
        else:
            print('The word "' + word + '" is not in the list')
            
        print('The port number is ' + str(port))
        
        print('Press enter to exit')
        
        input()
        
