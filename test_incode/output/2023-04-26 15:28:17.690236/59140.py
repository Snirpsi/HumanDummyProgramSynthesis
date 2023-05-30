#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and calculates a list of words. """    
    while True:
        port = input("Enter a port number: ")
        words = []
        
        for word in port2words(port):
            words.append(word)
            
        print(" ".join(words))
        
        if input("Continue? [y/N]").lower() == "y":
            break
        
    print("Done!")
    
