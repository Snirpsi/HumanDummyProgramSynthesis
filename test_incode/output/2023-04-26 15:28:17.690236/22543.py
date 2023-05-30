#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Open the file "words.txt" and read its contents into a list.
    with open('words.txt', 'r') as f:
        words = [word.strip() for word in f.readlines()]
        
    # Print the list to stdout.
    print('\n'.join(words))
    
    # Start the webserver.
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Start the webserver.
    httpd.serve_forever()
    
