#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and enumerates all ports. """    
    ports = enumerate_ports()
    
    for port in ports:
        remove_words_from_port(port)
        
    print("Done")

<|/ file source=github ext=.py |>