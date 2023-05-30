#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or calculates words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    wordlist = list(set(words))
    
    wordlist.sort()
    
    print('\nWordlist:')
    for word in wordlist:
        print(word)
    
    print('\nWordlist sorted:')
    for word in wordlist:
        print(word)
    
    print('\nWordlist reversed:')
    for word in wordlist[::-1]:
        print(word)
    
    print('\nWordlist unique:')
    for word in list(set(wordlist)):
        print(word)
    
    print('\nWordlist intersection:')
    
    wordlist1 = ['apple', 'banana', 'cherry']
    wordlist2 = ['apple', 'banana', 'cherry']
    
    wordlist3 = list(set(wordlist1).intersection(set(wordlist2)))
    
    print('\nWordlist intersection:')
    for word in wordlist3:
        print(word)
    
    print('\nWordlist difference:')
    
    wordlist1 = ['apple', 'banana', 'cherry']
    wordlist2 = ['apple', 'banana', 'cherry']
    
    wordlist3 = list(set(wordlist1).difference(set(wordlist2)))
    
    print('\nWordlist difference:')
    for word in wordlist3:
        print(word)
    
    print('\nWordlist symmetric difference:')
    
    wordlist1 = ['apple', 'banana', 'cherry']
    wordlist2 = ['apple', 'banana', 'cherry']
    
    wordlist3 = list(set(wordlist1).symmetric_difference(set(wordlist2)))
    
    print('\nWordlist symmetric difference:')
    for word in wordlist3:
        print(word)
    
    print('\nWordlist symmetric difference with duplicates:')
    
    wordlist1 = ['apple', 'banana', 'cherry']
    wordlist2 = ['apple', 'banana', 'cherry']
    
    wordlist3 = list(set(wordlist1).symmetric_difference(set(wordlist2), True))
    
    print('\nWordlist symmetric difference with duplicates:')
    for word in wordlist3:
        print(word)
    
    print('\nWordlist symmetric difference with duplicates and duplicates:')
    
    wordlist1 = ['apple', 'banana', 'cherry']
    wordlist2 = ['apple', 'banana', 'cherry']
    
    wordlist3 = list(set(wordlist1).symmetric_difference(set(wordlist2), True, True))
    
    print('\nWordlist symmetric difference with duplicates and duplicates:')
    for word in wordlist3:
        print(word)
    
    print('\nWordlist symmetric difference with duplicate