#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Open the file containing the words and store them in the list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.rstrip())
    
    # Start the server
    httpd = HTTPServer(('', 8080), WordsHandler)
    httpd.serve_forever()
    
