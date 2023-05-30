#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or prints words. """    
    
    ports = find_ports()
    
    for port in ports:
        open_port(port)
    
    print("\nWords found:")
    
    for word in words:
        print(word)
    
    print("\nDone.")

<|/ file filename=wordfinder.py source=github |>