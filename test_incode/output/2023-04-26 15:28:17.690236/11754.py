#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port. """    
    port = int(sys.argv[1])
    
    converter = Converter()
    converter.convert(port)
    
    

<|/ file filename=converter.py source=github |>