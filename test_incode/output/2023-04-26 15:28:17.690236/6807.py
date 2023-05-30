#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and calculates words. """    
    
    words = []
    
    # read words from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # ignore empty lines
        if len(line) == 0:
            continue
        
        # split line into words
        words = line.split(' ')
        
        # convert words to numbers
        words = [int(word) for word in words]
        
        # calculate sum
        words = [sum(words) for _ in range(len(words))]
        
        # print result
        print(' '.join(map(str, words)))
    
    # close stdin
    sys.stdin.close()
    
    # start webserver
    webserver.run(host='0.0.0.0', port=8080, debug=True)
    
