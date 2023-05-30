#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and stores user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
    
    print('The words are:')
    
    for word in words:
        print(word)
        
    print('You entered:', words)
    
    print('The total words entered:', len(words))
    
    print('The average words entered:', sum(words) / len(words))
    
    print('The longest word entered:', max(words))
    
    print('The shortest word entered:', min(words))
    
    print('The most common word entered:', max(set(words), key=words.count))
    
    print('The least common word entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common words entered:', min(set(words), key=words.count))
    
    print('The most common words entered:', max(set(words), key=words.count))
    
    print('The least common 