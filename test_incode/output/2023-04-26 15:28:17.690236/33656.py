#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = [
        'apple',
        'banana',
        'cat',
        'dog',
        'elephant',
        'horse',
        'lion',
        'monkey',
        'orange',
        'pig',
        'sheep',
        'tiger',
        'whale',
        'zebra',
    ]
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
    
