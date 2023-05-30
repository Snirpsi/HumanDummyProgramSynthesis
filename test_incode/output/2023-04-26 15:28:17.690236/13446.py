#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    words = [
        'apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe',
        'hamster', 'kangaroo', 'lion', 'monkey', 'orange', 'pig', 'rabbit',
        'sheep', 'tiger', 'whale', 'zebra', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish', 'zebrafish',
        'zebrafish', 'zebrafish', 'zebrafish