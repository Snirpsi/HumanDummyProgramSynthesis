#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and converts fruits. """    
    
    port = int(sys.argv[1])
    
    fruits = ("apple", "banana", "cherry")
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, FruitHandler)
    
    httpd.serve_forever()
