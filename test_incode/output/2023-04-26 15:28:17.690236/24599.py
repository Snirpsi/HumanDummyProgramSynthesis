#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    import sys
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    word_counts = [word for word, count in word_counts]
    
    for word, count in word_counts:
        print(word, count)
    
    
