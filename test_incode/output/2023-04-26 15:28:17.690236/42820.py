#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or opens words. """    
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
