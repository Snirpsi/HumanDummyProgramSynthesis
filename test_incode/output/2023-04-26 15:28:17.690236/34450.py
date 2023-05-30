#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words or stores a port. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Calculate port
    port = int(input('Enter a port number: '))
    
    # Print words and port
    print('Words: ', words)
    print('Port: ', port)
    
    # Calculate port and print result
    port_result = port * len(words)
    print('Port result: ', port_result)
    
    # Print result
    print('Result: ', port_result % 10)
    
    # Close file
    f.close()
    
    # Close program
    exit(0)
    
# End of program
