#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or iterates over a port. """    
    
    # Open the port and iterate over all words in it
    port = open("/dev/ttyUSB0", "rb")
    words = []
    while True:
        line = port.readline()
        if not line:
            break
        words.append(line.strip())
    
    # Close the port
    port.close()
    
    # Print the words to the screen
    for word in words:
        print(word)
        
    # Close the file
    file.close()
    
    # Close the terminal
    terminal.close()
    
    # Close the program
    exit(0)
