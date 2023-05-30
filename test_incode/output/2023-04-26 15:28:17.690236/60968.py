#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and calculates fruits. """    
    
    # Start a server
    server = HTTPServer(('', 8080), FruitCalculator)
    
    # Start a web server
    web = WebServer()
    web.serve_forever()
    
    # Stop the server
    server.socket.close()
    
    # Stop the web server
    web.socket.close()
    
