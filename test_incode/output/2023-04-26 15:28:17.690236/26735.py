#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and enumerates all ports. """    
    
    words = ['apple', 'banana', 'cherry']
    
    ports = []
    
    while True:
        
        word = ''.join(random.choice(words) for _ in range(