#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python remove-word.py <word>')
        sys.exit()
    
    word = sys.argv[1]
    
    print('removing word "' + word + '"')
    
    removeWord(word)
    
    print('calculating list of words')
    
    wordList = calculateWordList(word)
    
    print('removing words from list')
    
    removeWordsFromList(wordList)
    
    print('done')
    
    
