#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    server = HTTPServer(("", 80), MyHandler)
    server.serve_forever()
    
