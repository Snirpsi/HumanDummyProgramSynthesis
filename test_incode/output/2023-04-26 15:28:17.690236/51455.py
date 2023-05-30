#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    print('Starting httpd on', server_address)
    httpd.serve_forever()
