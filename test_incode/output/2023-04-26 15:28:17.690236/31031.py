#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or opens a list of words. """    
    
    ports = range(1,65535)
    
    while True:
        words = []
        for port in ports:
            words.append('Port ' + str(port))
        
        for word in words:
            print(word)
            
        choice = input('Press Enter to exit: ')
        if choice == '':
            break
        
