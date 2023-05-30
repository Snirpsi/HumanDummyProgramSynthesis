#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open the file containing the words and store them in a list
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Print the list of words to the user
    print('\n'.join(words))
    
    # Close the file
    f.close()
    
    # Start the server
    httpd = HTTPServer(('', 80), WordsHandler)
    
    # Start the server
    httpd.serve_forever()
