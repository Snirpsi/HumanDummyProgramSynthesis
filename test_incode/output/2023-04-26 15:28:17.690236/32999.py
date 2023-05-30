#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or adds a list of words. """    
    
    ports = []
    
    # Add words to the list
    words = ['word1', 'word2', 'word3']
    
    # Add ports to the list
    ports = [80, 8080, 8081]
    
    # Print the list
    print('\n'.join(words))
    print('\n'.join(ports))
    
    # Start the server
    httpd = make_server('', 8080, make_handler