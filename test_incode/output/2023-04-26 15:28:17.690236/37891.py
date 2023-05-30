#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveUserInputHandler)
    httpd.serve_forever()
    
