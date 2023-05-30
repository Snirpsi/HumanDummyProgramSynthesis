#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input or enumerates words. """    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        for word in sys.argv[1:]:
            words.append(word)
    else:
        words = list(enumerate(' '.join(sys.argv[1:])))
    
    for index, word in enumerate(words):
        print('{}. {}'.format(index+1, word[0]))
        print('{}. {}'.format(index+1, word[1]))
        print('{}. {}'.format(index+1, word[2]))
        print('{}. {}'.format(index+1, word[3]))
        print('{}. {}'.format(index+1, word[4]))
        print('{}. {}'.format(index+1, word[5]))
        print('{}. {}'.format(index+1, word[6]))
        print('{}. {}'.format(index+1, word[7]))
        print('{}. {}'.format(index+1, word[8]))
        print('{}. {}'.format(index+1, word[9]))
        print('{}. {}'.format(index+1, word[10]))
        print('{}. {}'.format(index+1, word[11]))
        print('{}. {}'.format(index+1, word[12]))
        print('{}. {}'.format(index+1, word[13]))
        print('{}. {}'.format(index+1, word[14]))
        print('{}. {}'.format(index+1, word[15]))
        print('{}. {}'.format(index+1, word[16]))
        print('{}. {}'.format(index+1, word[17]))
        print('{}. {}'.format(index+1, word[18]))
        print('{}. {}'.format(index+1, word[19]))
        print('{}. {}'.format(index+1, word[20]))
        print('{}. {}'.format(index+1, word[21]))
        print('{}. {}'.format(index+1, word[22]))
        print('{}. {}'.format(index+1, word[23]))
        print('{}. {}'.format(index+1, word[24]))
        print('{}. {}'.format(index+1, word[25]))
        print('{}. {}'.format(index+1, word[26]))
        print('{}. {}'.format(index+1, word[27]))
        print('{}. {}'.format(index+1, word[28]))
        print('{}. {}'.format(index+1, word[29]))
        print('{}. {}'.format(index+1, word[30]))
        print('{}. {}'.format(index+1, word[31]))
        print('{}. {}'.format(index+1, word[32]))
        print('{}. {}'.format(index+1, word[33]))
        print('{}. {}'.format(index+1, word[34]))
        print('{}. {}'.format(index+1, word[35]))
        print('{}. {}'.format(index+1, word[36]))
        print('{}. {}'.format(index+1, word[37]))
        print('{}. {}'.format(index+1, word[38]))
        print('{}. {}'.format(index+1, word[39]))
        print('{}. {}'.format(index+1, word[40]))
        print('{}. {}'.format(index+1, word[41]))
        print('{}. {}'.format(index+1, word[42]))
        print('{}. {}'.format(index+1, word[43