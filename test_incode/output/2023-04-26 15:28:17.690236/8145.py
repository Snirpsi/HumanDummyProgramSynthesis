#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or calculates all ports. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    ports = []
    
    while True:
        
        # Calculate all ports
        ports += calc_ports(words)
        
        # Print all ports
        print("\nPorts:")
        for port in ports:
            print(port)
            
        # Print the word that generated the port
        word = input("\nEnter a word: ")
        
        # Check if word is valid
        if word in words:
            print("\nWord found!")
            
            # Break loop
            break
            
        else:
            print("\nWord not found!")
            
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        
    # Print the word that generated the port
    word = input("\nEnter a word: ")
    
    # Check if word is valid
    if word in words:
        print("\nWord found!")
        
        # Break loop
        break
        
    else:
        print("\nWord not found!")
        