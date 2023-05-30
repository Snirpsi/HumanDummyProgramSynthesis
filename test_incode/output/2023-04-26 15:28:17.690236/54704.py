#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or multiplyes all ports. """    
    
    # Read words from stdin
    words = [line.strip() for line in sys.stdin]
    
    # Iterate over words
    for word in words:
        
        # Multiply all ports
        ports = word.split(',')
        
        # Iterate over ports
        for port in ports:
            
            # Print the result
            print('{} * {}'.format(port, word))
            
        # Print the result
        print('{} * {}'.format(word, port))
        
        # Print the result
        print('{} * {}'.format(word, port