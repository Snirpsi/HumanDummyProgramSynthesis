#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python add_words_to_file.py <words_file>')
        exit(1)
    
    words = open(sys.argv[1], 'r')
    
    words = words.read().split()
    
    words_to_add = []
    
    for word in words:
        
        if word not in words_to_add:
            words_to_add.append(word)
    
    words_to_add = sorted(words_to_add)
    
    words_to_add = words_to_add[::-1]
    
    words_to_add = ' '.join(words_to_add)
    
    words = words.read().split()
    
    words.extend(words_to_add)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().split()
    
    words.extend(words_to_write)
    
    words_to_write = ' '.join(words)
    
    words = words.read().