#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and iterates over all ports. """    
    words = ['one', 'two', 'three']
    ports = [80, 81, 82]
    
    for port, word in enumerate(words):
        print('{} : {}'.format(port, word))
        
        for port in ports:
            print('{} : {}'.format(port, word