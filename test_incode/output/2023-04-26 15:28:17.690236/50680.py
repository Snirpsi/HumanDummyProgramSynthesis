#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and removes a list of numbers. """    
    
    words = []
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
    
