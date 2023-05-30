#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words = list(set(words))
    
    words.sort()
    
    word_count = len(words)
    
    print("Words: ", word_count)
    
    print("Words with frequency > 1: ", len([w for w in words if len(w) > 1]))
    
    print("Words with frequency < 1: ", len([w for w in words if len(w) < 1]))
    
    print("Words with frequency == 1: ", len([w for w in words if len(w) == 1]))
    
    print("Words with frequency > 1 and frequency < 1: ", len([w for w in words if len(w) > 1 and len(w) < 1]))
    
    print("Words with frequency == 1 and frequency > 1: ", len([w for w in words if len(w) == 1 and len(w) > 1]))
    
    print("Words with frequency > 1 and frequency == 1: ", len([w for w in words if len(w) > 1 and len(w) == 1]))
    
    print("Words with frequency > 1 and frequency > 1 and frequency == 1: ", len([w for w in words if len(w) > 1 and len(w) > 1 and len(w) == 1]))
    
    print("Words with frequency > 1 and frequency > 1 and frequency > 1 and frequency == 1: ", len([w for w in words if len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) == 1]))
    
    print("Words with frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency == 1: ", len([w for w in words if len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) == 1]))
    
    print("Words with frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency == 1: ", len([w for w in words if len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) > 1 and len(w) == 1]))
    
    print("Words with frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency > 1 and frequency == 1: ", len([w for w in words if len(