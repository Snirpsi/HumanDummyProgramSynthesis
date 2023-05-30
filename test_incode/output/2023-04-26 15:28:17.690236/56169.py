#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or multiplyes a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ports = range(101, 104)
    
    while True:
        ports = list(map(lambda x: int(x) * int(words[x]), ports))
        
        print('\n'.join(map(str, ports)))
        
        time.sleep(1)
        
