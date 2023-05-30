#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    for x in range(0, 10):
        numbers.append(x)
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
