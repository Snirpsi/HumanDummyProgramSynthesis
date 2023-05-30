#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    with open('words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
    
    print('Done!')
    
