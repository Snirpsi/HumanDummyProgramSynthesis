#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and prints all ports. """    
    
    server_address = ("", 80)
    httpd = make_server(*server_address, SimpleHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
    
