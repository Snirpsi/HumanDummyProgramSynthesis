#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or returns a list of numbers. """    
    port = int(sys.argv[1])
    webserver_class = Webserver
    webserver_class.port = port
    webserver_class.run()
