#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or iterates over a list of words. """    
    
    words = ['word1', 'word2', 'word3']
    
    # start server
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
    
    # print user input
    word = None
    while word not in words:
        word = input('Enter a word: ')
        print('You entered', word)
    
    # iterate over words
    for word in words:
        print('You entered', word)
        
    # quit server
    httpd.shutdown()
    httpd.server_close()
    
