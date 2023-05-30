#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and removes numbers. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Open the wordlist
    with open('wordlist.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Remove numbers
    words = [word for word in words if word.isdigit()]
    
    # Print the list
    print('\n'.join(words))
    
    # Start the webserver
    httpd = HTTPServer(('', port), WordsHandler)
    
    # Start the webserver
    httpd.serve_forever()
