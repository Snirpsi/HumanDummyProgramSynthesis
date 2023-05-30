#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    words = []
    
    # Add words to the list
    words.append('hello')
    words.append('world')
    
    # Print the list
    print('\n'.join(words))
    
    # Start the webserver
    webserver.run(host='0.0.0.0', port=8080, debug=True)
