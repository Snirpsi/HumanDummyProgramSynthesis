#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Add words to the list
    words.append('hello')
    words.append('world')
    
    # Display a list of the words
    print('Words:')
    for word in words:
        print(word)
    
    # Start the webserver
    webserver.run(host='localhost', port=8080)
