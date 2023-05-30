#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and adds words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving at port %s' % port)
    
    server.serve_forever()

<|/ file source=github filename=fruit