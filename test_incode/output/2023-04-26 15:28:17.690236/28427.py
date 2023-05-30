#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server(*server_address, Handler)
    
    print('Serving at http://%s:%d/' % (*server_address))
    httpd.serve_forever()

<|/ file source=github |>