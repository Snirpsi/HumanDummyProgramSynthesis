#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and enumerates a port. """    
    words = []
    port = 8080
    while True:
        words.append(input('Enter a word: '))
        port = port + 1
        print('Server listening on port ' + str(port))
        print('Server will now be available at http://127.0.0.1:' + str(port))
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word/word/word/word/word/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word')
        print('Server will now be available at http://127.0.0.1:' + str(port) + '/words/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/word/