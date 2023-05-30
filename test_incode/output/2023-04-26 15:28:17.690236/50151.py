#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores all ports or prints a list of words. """    
    
    # Check if a port is available
    if sys.argv[1] in ports:
        ports[sys.argv[1]] = True
    else:
        ports[sys.argv[1]] = False
    
    # Print the list of ports
    for port in ports:
        print("Port {} is available".format(port))
    
    # Print the list of words
    for word in words:
        print("Word {} is available".format(word))
    
    # Print the list of words with no ports
    for word in words:
        if words[word] is None:
            print("Word {} has no ports".format(word))
    
    # Print the list of words with ports
    for word in words:
        if words[word] is not None:
            print("Word {} has ports".format(word))
    
    # Print the list of words with ports and no words
    for word in words:
        if words[word] is not None and words[word] is not True:
            print("Word {} has ports and no words".format(word))
    
    # Print the list of words with ports and ports
    for word in words:
        if words[word] is not None and words[word] is not False:
            print("Word {} has ports and ports".format(word))
    
    # Print the list of words with ports and ports and no words
    for word in words:
        if words[word] is not None and words[word] is not True and words[word] is not False:
            print("Word {} has ports and ports and no words".format(word))
    
    # Print the list of words with ports and ports and ports
    for word in words:
        if words[word] is not None and words[word] is not True and words[word] is not None and words[word] is not False:
            print("Word {} has ports and ports and ports".format(word))
    
    # Print the list of words with ports and ports and ports and no words
    for word in words:
        if words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not True and words[word] is not None and words[word] is not False:
            print("Word {} has ports and ports and ports and no words".format(word))
    
    # Print the list of words with ports and ports and ports and ports
    for word in words:
        if words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not True and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not None and words[word] is not False:
            print("Word {} has 