#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ['word1', 'word2', 'word3']
    
    port = 5000
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting server at http://%s:%s/' % (server_address[0], server_address[1]))
    
    httpd.serve_forever()
    
