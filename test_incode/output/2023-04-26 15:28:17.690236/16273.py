#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or enumerates fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
    if len(words) == 0:
        words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'watermelon', 'lime', 'mango', 'grapefruit', 'peach', 'pineapple', 'plum', 'plums', 'apples', 'bananas', 'oranges', 'grapes', 'kiwis', 'watermelons', 'limes', 'mangoes', 'grapefruits', 'peaches', 'pineapples', 'plums', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', 'watermelonses', 'limeses', 'mangoes', 'grapefruitses', 'peacheses', 'pineappleses', 'plumses', 'plumses', 'appleses', 'bananasses', 'orangeses', 'grapeses', 'kiwisses', '