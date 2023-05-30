#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and prints numbers. """    
    
    words = []
    
    # Add words to the list
    words.append("hello")
    words.append("world")
    
    # Print the list
    print(words)
    
    # Start a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Run the server
    server.serve_forever()
    
