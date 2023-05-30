#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    httpd = make_server(server_address, MyHandler)
    
    print("Serving at http://%s:%s" % (server_address[0], server_address[1]))
    
    httpd.serve_forever()
