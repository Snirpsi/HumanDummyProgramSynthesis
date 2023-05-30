#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or iterates over words. """    
    ports = range(8000, 8100)
    
    for port in ports:
        webbrowser.open_new('http://127.0.0.1:%s' % port)
        
