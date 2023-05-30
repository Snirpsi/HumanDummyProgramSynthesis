#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port. """    
    while True:
        port = int(input('Enter a port number: '))
        
        # Multiply port by 2
        port *= 2
        
        # Print the result
        print('The port number multiplied by 2 is', port)
        
        # Sleep for 1 second
        time.sleep(1)
        
        # Exit the loop
        if port == 1000:
            break
        
