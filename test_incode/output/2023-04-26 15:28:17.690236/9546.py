#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    # Create a server that listens on port 8000
    httpd = HTTPServer(('', port), MyHandler)
    
    # Run the server
    httpd.serve_forever()
    
    # Stop the server
    httpd.shutdown()
    
    # Print the port and list of words
    print('The port is ' + str(port))
    print('The list of words is ' + str(words))
    
