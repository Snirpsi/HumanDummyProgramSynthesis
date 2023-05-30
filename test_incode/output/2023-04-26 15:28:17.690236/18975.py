#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = HTTPServer(('localhost', port), MyHandler)
    web.serve_forever()
    
