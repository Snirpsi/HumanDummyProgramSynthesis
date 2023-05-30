#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and enumerates a port. """    
    
    # Read command line arguments
    port = int(sys.argv[1])
    
    # Read words from file
    words = []
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    # Remove words and enumerate port
    words = list(set(words))
    
    # Print results
    print('\n'.join(words))
    print('Port: ' + str(port))
    
    # Close file
    words.close()
    
    # Close port
    port.close()
    
    # Close program
    sys.exit()
    
