#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or converts numbers. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        webbrowser.open_new('http://127.0.0.1:%s' % port)
    
    
<|/ file filename=server.py |>