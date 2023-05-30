#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and removes user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveNumbersHandler)
    httpd.serve_forever()
    
