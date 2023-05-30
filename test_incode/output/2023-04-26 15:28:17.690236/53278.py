#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or prints words. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), MyHandler)
    webserver.serve_forever()
    
