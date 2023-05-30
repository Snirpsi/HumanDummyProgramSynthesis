#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and stores user input. """    
    
    # Start a server
    server = HTTPServer(('', 80), Handler)
    
    # Start a web browser
    webbrowser.open('http://localhost:80')
    
    # Wait for user input
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
