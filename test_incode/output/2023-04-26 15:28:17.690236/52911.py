#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = ports * 2
    print('\n'.join(str(i) for i in ports))
    
<|/ file source=github filename=port