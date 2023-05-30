#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or stores words. """    
    
    port = int(sys.argv[1])
    
    # Store words in a file
    with open('words.txt', 'w') as f:
        for word in words:
            f.write('%s\n' % word)
    
    # Print the port
    print('Server running at port %d' % port)
    
    # Run the server
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py |>