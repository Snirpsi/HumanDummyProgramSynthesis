#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and calculates a port. """    
    
    # read input from stdin
    words = sys.stdin.read().split()
    
    # create a list of words and a dictionary
    words = list(map(str.strip, words))
    word_dict = dict(zip(words, range(len(words))))
    
    # enumerate words and calculate port
    port = 0
    for word in words:
        port += word_dict[word]
    
    # print result
    print("Port is {}".format(port))
