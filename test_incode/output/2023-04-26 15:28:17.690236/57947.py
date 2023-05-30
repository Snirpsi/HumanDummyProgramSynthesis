#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    print("Adding word %s..." % word)
    
    with open('words.txt', 'a') as wordfile:
        wordfile.write(word + '\n')
    
    print("Done.")
    
