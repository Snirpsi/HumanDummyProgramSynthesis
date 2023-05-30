#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
