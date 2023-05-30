#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = [
        'apple',
        'banana',
        'cat',
        'dog',
        'elephant',
        'fox',
        'goat',
        'horse',
        'lion',
        'monkey',
        'pig',
        'rabbit',
        'sheep',
        'tiger',
        'whale'
    ]
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
