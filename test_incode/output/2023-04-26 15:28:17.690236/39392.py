#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or stores all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[0]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[1]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[2]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[3]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[4]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[5]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[6]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[7]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[8]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[9]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[10]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[11]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for connections
    httpd = HTTPServer(('', ports[12]), MyHandler)
    httpd.serve_forever()
    
    # Open a web server and listen for 