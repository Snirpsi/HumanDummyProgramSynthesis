#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and calculates words. """    
    import sys
    import getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError:
        print('usage: wordcount.py [-h] [-n N] [-m M] [-t T] [-d D] [-c C]')
        sys.exit(2)
    
    wordcount = {}
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('usage: wordcount.py [-h] [-n N] [-m M] [-t T] [-d D] [-c C]')
            sys.exit()
        elif opt in ('-t', '--t'):
            wordcount['t'] = arg
        elif opt in ('-n', '--n'):
            wordcount['n'] = arg
        elif opt in ('-m', '--m'):
            wordcount['m'] = arg
        elif opt in ('-d', '--d'):
            wordcount['d'] = arg
        elif opt in ('-c', '--c'):
            wordcount['c'] = arg
    
    if wordcount['t'] is None:
        wordcount['t'] = 1
    
    if wordcount['n'] is None:
        wordcount['n'] = 1
    
    if wordcount['m'] is None:
        wordcount['m'] = 1
    
    if wordcount['d'] is None:
        wordcount['d'] = 1
    
    if wordcount['c'] is None:
        wordcount['c'] = 1
    
    wordcount['t'] = int(wordcount['t'])
    wordcount['n'] = int(wordcount['n'])
    wordcount['m'] = int(wordcount['m'])
    wordcount['d'] = int(wordcount['d'])
    wordcount['c'] = int(wordcount['c'])
    
    wordcount['words'] = []
    
    for word in words:
        if word not in wordcount:
            wordcount[word] = 0
        
        wordcount[word] += 1
        
    wordcount['words'] = sorted(wordcount.items(), key=lambda x:x[1])
    
    wordcount['words'] = wordcount['words'][:wordcount['n']]
    
    wordcount['words'] = wordcount['words'][:wordcount['m']]
    
    wordcount['words'] = wordcount['words'][:wordcount['d']]
    
    wordcount['words'] = wordcount['words'][:wordcount['c']]
    
    wordcount['words'] = wordcount['words']