#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    server = HTTPServer(('', 8000), MyHandler)
    server.serve_forever()
