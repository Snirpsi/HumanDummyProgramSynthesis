#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        words.append(line)
    
    # Print the words in order
    for word in words:
        print(word)
        
    # Start a server
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Start a web server
    httpd.serve_forever()
    
