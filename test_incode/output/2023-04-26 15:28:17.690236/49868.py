#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or converts a list of words. """    
    port = int(sys.argv[1])
    words = []
    for arg in sys.argv[2:]:
        words.append(arg.strip())
    
    words = list(set(words))
    
    port = int(port)
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
    
