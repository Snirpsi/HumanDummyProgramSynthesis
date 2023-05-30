#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or stores words. """    
    port = int(sys.argv[1])
    words = []
    
    # Remove port from URL
    if port != 80:
        words.append(sys.argv[2])
    else:
        words.append(sys.argv[3])
    
    # Store words in file
    with open('words.txt', 'w') as f:
        f.writelines(words)
    
    # Print words to terminal
    print('\n'.join(words))
    
    # Close file
    f.close()
    
    # Start webserver
    webserver()
    
