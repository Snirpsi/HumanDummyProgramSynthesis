#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    try:
        words = open(sys.argv[1]).read().splitlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    
    ports = [port]
    
    for port in ports:
        server = HTTPServer(('', port), WordsServer)
        server.serve_forever()
    
