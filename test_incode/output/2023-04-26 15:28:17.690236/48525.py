#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    numbers = []
    
    # Read numbers from stdin
    while True:
        line = input('Enter a number: ')
        if not line:
            break
        numbers.append(int(line))
    
    # Print the list
    print('\n'.join(map(str, numbers)))
    
    # Close the connection
    connection.close()
    
