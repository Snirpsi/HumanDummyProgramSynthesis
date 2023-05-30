#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or prints a port. """    
    import sys
    
    words_to_remove = []
    
    for word in sys.argv[1:]:
        if word in ['-a', '--all']:
            words_to_remove.extend(sys.argv[1:])
        else:
            words_to_remove.append(word)
    
    words_to_remove = set(words_to_remove)
    
    for word in words_to_remove:
        sys.stdout.write(word + ' ')
    
    sys.stdout.write('\n')
    
    if len(words_to_remove) == 0:
        sys.stdout.write('No words removed\n')
    else:
        sys.stdout.write('Removed 