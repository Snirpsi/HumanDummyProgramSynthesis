#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Convert input into number
        number = int(sys.argv[1])
        
        # Iterate over user input
        for letter in sys.argv[2:]:
            
            # Convert input into number
            number = int(letter)
            
            # Print the number
            print(number)
            
    else:
        
        # Print the number
        print(