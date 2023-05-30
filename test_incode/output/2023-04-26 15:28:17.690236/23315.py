#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and opens a list of words. """    
    
    words = ['word1', 'word2', 'word3']
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Serving on port 8000...')
    httpd.serve_forever()
    
