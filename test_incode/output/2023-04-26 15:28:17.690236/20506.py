#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or stores a port. """    
    port = int(sys.argv[1])
    
    if port == -1:
        print("Please specify a port to convert.")
    else:
        convert_port(port)
    
<|/ file filename=portconvert.py ext=.py |>