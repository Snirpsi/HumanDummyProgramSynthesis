#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or converts a port. """    
    
    port = int(sys.argv[1])
    
    if port == 80:
        webbrowser.open_new('http://localhost')
    elif port == 443:
        webbrowser.open_new('https://