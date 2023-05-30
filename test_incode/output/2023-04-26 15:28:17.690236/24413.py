#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    ports = [int(x) for x in sys.argv[1:]]
    
    for port in ports:
        convert_port(port)
        
    print("Done.")

<|/ file filename=portconvert.py ext=.py |>