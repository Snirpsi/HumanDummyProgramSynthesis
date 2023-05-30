#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or stores all ports. """    
    
    ports = [8080, 8081, 8082]
    
    # Start webserver
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
    
    # 