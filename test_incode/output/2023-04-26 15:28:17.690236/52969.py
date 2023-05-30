#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and removes a list of words. """    
    port = int(sys.argv[1])
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, WordsHandler)
    httpd.serve_forever()
    
    
