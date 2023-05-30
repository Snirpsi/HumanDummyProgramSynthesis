#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and stores words. """    
    while True:
        words = []
        
        # Read words from file
        with open('words.txt', 'r') as f:
            words = f.read().splitlines()
            
        # Print words to screen
        print('\n'.join(words))
        
        # Print words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # Print list of words to screen
        print('\n'.join(words))
        
        # Print list of words to file
        with open('words.txt', 'w') as f:
            f.write('\n'.join(words))
        
        # Wait for user to enter a word
        word = input('Enter a word: ')
        
        # Append word to list of words
        words.append(word)
        
        # 