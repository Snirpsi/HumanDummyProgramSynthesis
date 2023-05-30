#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and converts words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <file> <file> ...' % sys.argv[0])
        sys.exit()
    
    for file in sys.argv[1:]:
        with open(file) as infile:
            for line in infile:
                line = line.strip()
                if line:
                    line = line.split()
                    words = [word for word in line if word]
                    
                    for word in words:
                        word = word.strip()
                        if word:
                            word = word.lower()
                            if word:
                                word = word.replace(' ', '')
                                word = word.title()
                                
                                outfile.write(word + '\n')
