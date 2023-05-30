#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and iterates over words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == '':
            break
        
        words.append(word)
        
    print('The words are:')
    
    for word in words:
        print(word)
        
    print('\nThe word that occurs most often is:', 
          sorted(words, key=words.count)[0])
    
    print('\nThe word that occurs least often is:', 
          sorted(words, key=words.count)[1])
    
    print('\nThe word that occurs most often and least often is:', 
          sorted(words, key=words.count, reverse=True)[0])
    
    print('\nThe word that occurs least often and most often is:', 
          sorted(words, key=words.count, reverse=True)[1])
    
    print('\nThe word that occurs most often and least often and most often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-2:])
    
    print('\nThe word that occurs least often and most often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[:-2])
    
    print('\nThe word that occurs most often and least often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-3:])
    
    print('\nThe word that occurs least often and most often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[:-3])
    
    print('\nThe word that occurs most often and least often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-4:])
    
    print('\nThe word that occurs least often and most often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[:-4])
    
    print('\nThe word that occurs most often and least often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-5:])
    
    print('\nThe word that occurs least often and most often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[:-5])
    
    print('\nThe word that occurs most often and least often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-6:])
    
    print('\nThe word that occurs least often and most often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[:-6])
    
    print('\nThe word that occurs most often and least often and least often is:', 
          sorted(words, key=words.count, 
                 reverse=True)[-7:])
    
    print('\nThe word that occurs least often and most often and least often 