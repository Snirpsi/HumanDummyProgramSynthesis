#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and returns a port. """    
    port = []
    
    # Open the port
    with open('port', 'w') as portFile:
        portFile.write(''.join(str(x) for x in port))
        
    # Close the port
    portFile.close()
    
    # Return the port
    return port
<|/ file filename=portGenerator.py dstars=0 |>