#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and removes words. """    
    ports = [int(i) for i in sys.argv[1:]]
    remove = set(sys.argv[2:])
    for port in ports:
        httpd = make_server('localhost', port, app)
        httpd.serve_forever()
    httpd.server_close()
    
