#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
