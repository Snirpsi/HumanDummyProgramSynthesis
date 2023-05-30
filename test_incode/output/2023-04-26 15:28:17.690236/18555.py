#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or adds fruits. """    
    
    port = int(sys.argv[1])
    fruits = ['apple', 'banana', 'cherry']
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()

<|/ file filename=