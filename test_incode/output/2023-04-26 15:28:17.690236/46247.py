#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and removes words. """    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        words = [word.strip() for word in wordFile.readlines()]
    
    words = [word for word in words if word not in words]
    
    with open('words.txt', 'w') as wordFile:
        wordFile.writelines(words)
        
    print('Words successfully deleted.')
    
