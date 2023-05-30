#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and stores numbers. """    
    
    words = []
    
    # Read the words from a file
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    # Print the words and numbers in the file
    print('\n'.join(words))
    print('\n'.join(map(str, list(range(1, 1001)))))
    
    # Start the webserver
    httpd = HTTPServer(('', 8080), MyHandler)
    
    # Run the webserver
    httpd.serve_forever()
    
