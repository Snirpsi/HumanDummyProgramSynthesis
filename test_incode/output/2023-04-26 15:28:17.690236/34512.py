#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or calculates fruits. """    
    
    server_address = ("", 8000)
    
    httpd = HTTPServer(server_address, FruitCalculator)
    httpd.serve_forever()
    
