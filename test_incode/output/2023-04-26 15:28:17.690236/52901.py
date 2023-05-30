#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    words = ['word1', 'word2', 'word3']
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
