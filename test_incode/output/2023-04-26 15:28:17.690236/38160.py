#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and iterates over a list of words. """    
    ports = range(5000, 5999)
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    for port in ports:
        httpd = HTTPServer(('', port), MyHandler)
        httpd.serve_forever()
