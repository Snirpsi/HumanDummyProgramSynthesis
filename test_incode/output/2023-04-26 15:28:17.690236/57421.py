#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and stores words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
