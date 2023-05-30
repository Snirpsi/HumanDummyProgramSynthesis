#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and prints all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        webbrowser.open_new(f'http://localhost:{port}')
    print('All ports open.')
