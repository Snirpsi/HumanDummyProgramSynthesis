#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or prints a port. """    
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '-r':
            remove()
        else:
            print_port()
    else:
        print_port()

<|/ file filename=remove.py source=github |>