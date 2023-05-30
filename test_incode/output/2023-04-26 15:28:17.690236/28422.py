#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words and adds a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words = words + line.split(' ')
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in stopwords]
    
    with open('words.txt', 'w') as file:
        file.write('\n'.join(words))
        
    print('Done!')

