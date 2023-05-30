#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            
            if len(line) > 0:
                words.append(line)
    
    words.sort()
    
    word_count = len(words)
    
    print('Number of words: ' + str(word_count))
    
    for word in words:
        print(word)
    
    print('')
    
    print('Average word length: ' + str(word_count/len(words)))
    
    print('')
    
    print('Word count:')
    
    for word in words:
        print(word)
    
    print('')
    
    print('Word length:')
    
    for word in words:
        print(len(word))
    
    print('')
    
    print('Word frequency:')
    
    for word in words:
        print(word.count('