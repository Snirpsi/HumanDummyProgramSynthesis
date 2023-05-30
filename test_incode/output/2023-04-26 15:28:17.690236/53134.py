#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or returns a list of words. """    
    
    ports = remove_ports()
    
    if ports:
        words = remove_words(ports)
        
        if words:
            print(words)
        else:
            print("No words found")
    else:
        print("No ports found")
        
