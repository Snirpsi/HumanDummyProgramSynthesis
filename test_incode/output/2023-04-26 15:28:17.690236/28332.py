#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and returns all ports. """    
    ports = range(5000, 5050)
    for port in ports:
        print("Starting port {}".format(port))
        webbrowser.open_new('http://127.0.0.1:{}'.format(port))
    
