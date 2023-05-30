#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port and multiplyes a list of words. """    
    port = 1
    while True:
        port = port + 1
        print("Port {}".format(port))
        words = ["word1", "word2"]
        for word in words:
            print(word * port)
