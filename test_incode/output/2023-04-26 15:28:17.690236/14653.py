#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or removes a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    httpd = make_server(*server_address, RequestHandler)
    
    print("Serving at http://%s:%s" % (server_address[0], server_address[1]))
    httpd.serve_forever()
    
    
