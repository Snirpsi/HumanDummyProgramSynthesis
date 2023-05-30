#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        for line in wordFile:
            words.append(line.strip())
    
    words = list(set(words))
    
    words.sort()
    
    wordFile.close()
    
    wordFile.seek(0)
    
    wordFile.write('\n'.join(words))
    
    wordFile.truncate()
    
    wordFile.seek(0)
    
    wordFile.write('\n\n')
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.write('\n\n')
    
    wordFile.write('\n'.join(words))
    
    wordFile.