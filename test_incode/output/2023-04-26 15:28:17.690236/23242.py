#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveNumbersHandler)
    httpd.serve_forever()
    
