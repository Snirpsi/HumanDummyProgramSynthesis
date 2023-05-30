#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and converts words. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, handle_request)
    httpd.serve_forever()
    
