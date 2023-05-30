#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Read the file into a list
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Print the list of words
    print(words)
    
    # Start the server
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Run the server
    httpd.serve_forever()
    
