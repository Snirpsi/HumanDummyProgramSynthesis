#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit(1)
    
    word = sys.argv[1]
    
    print("Adding %s to your dictionary." % word)
    
    word_list = word.split()
    
    word_list.append("_")
    
    for word in word_list:
        