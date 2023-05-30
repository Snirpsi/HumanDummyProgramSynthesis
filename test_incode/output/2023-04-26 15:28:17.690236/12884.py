#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0] != '#']
    
    words = [word for word in words if word[0] != '!']
    
    words = [word for word in words if word[0] != '?']
    
    words = [word for word in words if word[0] != '@']
    
    words = [word for word in words if word[0] != '&']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    words = [word for word in words if word[0] != '+']
    
    words = [word for word in words if word[0] != '*']
    
    words = [word for word in words if word[0] != '-']
    
    word