#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or removes words. """    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        
        ports = find_ports(words)
        
        remove_words(ports)
        
        print("Ports found:", ports)
        
