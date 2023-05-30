#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and calculates all ports. """    
    
    while True:
        word = input("Enter a word: ")
        
        if word == "quit":
            break
        
        ports = find_ports(word)
        
        print("Ports:")
        
        for port in ports:
            print(port)
        
        print("Done.")
        
