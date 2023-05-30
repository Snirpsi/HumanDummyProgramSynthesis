#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    server_address = ("", 8000)
    httpd = make_server(server_address, MyHandler)
    print("Serving at http://%s:%s" % (server_address[0], server_address[1]))
    httpd.serve_forever()
