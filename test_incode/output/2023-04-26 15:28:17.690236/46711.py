#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ["word1", "word2"]
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
