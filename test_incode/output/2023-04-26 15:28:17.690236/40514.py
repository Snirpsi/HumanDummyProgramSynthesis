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
        'rabbit',
        'sheep',
        'tiger',
        'whale',
        'zebra',
    ]
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()
    
