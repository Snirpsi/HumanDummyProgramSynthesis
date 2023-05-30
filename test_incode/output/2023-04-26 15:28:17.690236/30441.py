#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or converts numbers. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word.isalpha():
            words.append(word)
        else:
            try:
                number = int(word)
                words.append(str(number))
            except ValueError:
                print('That is not a number')
                
    print('The words are:')
    print(words)
    
    print('The sum of the words is {}'.format(sum(words)))
    
    print('The average of the words is {}'.format(float(sum(words)) / len(words)))
    
    print('The most common word is {}'.format(max(words)))
    
    print('The least common word is {}'.format(min(words)))
    
    print('The word with the largest number of occurrences is {}'.format(max(words)))
    
    print('The word with the smallest number of occurrences is {}'.format(min(words)))
    
    print('The word with the greatest number of occurrences is {}'.format(max(words)))
    
    print('The word with the least number of occurrences is {}'.format(min(words)))
    
    print('The word with the greatest number of occurrences is the most common word')
    
    print('The word with the least number of occurrences is the least common word')
    
    print('The word with the greatest number of occurrences is the word with the greatest number of occurrences')
    
    print('The word with the least number of occurrences is the word with the least number of occurrences')
    
    print('The word with the greatest number of occurrences is the word with the greatest number of occurrences is the most common word')
    
    print('The word with the least number of occurrences is the word with the least number of occurrences is the least common word')
    
    print('The word with the greatest number of occurrences is the word with the greatest number of occurrences is the word with the greatest number of occurrences is the least common word')
    
    print('The word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least number of occurrences is the word with the least 