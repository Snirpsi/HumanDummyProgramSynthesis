#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and opens a port. """    
    
    words = ["word1", "word2", "word3", "word4"]
    
    port = open("/tmp/words.txt", "w")
    
    for word in words:
        port.write(word + "\n")
    
    port.close()
    
    print("Done")
    
