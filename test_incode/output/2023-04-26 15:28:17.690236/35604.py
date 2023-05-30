#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or stores all ports. """    
    ports = []
    
    # Start a server that listens on all available ports
    httpd = HTTPServer(('', 0), Handler)
    
    # Start a server that listens on a specific port
    httpd = HTTPServer(("", 8080), Handler)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    
    # Start a server that listens on a specific port and stop
    httpd = HTTPServer(("", 8080), StoppableHTTPServer)
    
    # Start a server that listens on all available ports and then stop
    httpd = HTTPServer(("", 0), StoppableHTTPServer)
    