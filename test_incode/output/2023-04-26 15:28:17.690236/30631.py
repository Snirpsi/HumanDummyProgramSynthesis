#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words or adds a port. """    
    
    words = []
    
    # Open the words and add them to the list
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.rstrip())
    
    # Print the list of words to the screen
    print(words)
    
    # Add the words to the port
    port = 'COM1'
    
    # Open the port and write to the port
    with serial.Serial(port, 9600, timeout=1) as ser:
        ser.write(words)
        
    # Print the port to the screen
    print(port)
    
    # Close the port
    ser.close()
    
    # Close the serial port
    ser = None
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit(0)
    
    # Close the program
    exit