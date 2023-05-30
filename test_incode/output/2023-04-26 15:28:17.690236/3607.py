#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and enumerates all ports. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    
    for port in enumerate_ports(words):
        print(port)
        
