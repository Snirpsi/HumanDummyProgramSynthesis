#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port and calculates words. """    
    port = 8080
    words = []
    
    # Create a server to listen for connections
    server = HTTPServer(("", port), WordsHandler)
    
    # Start a server
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
    # Print the list of words
    for word in words:
        print(word)
    
    # Print the port number
    print("The port number is", port)
    
    # Close the server
    server.socket.close()
    
    # Close the program
    