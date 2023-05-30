#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    
    words = ['apple', 'banana', 'carrot', 'dog', 'elephant', 'horse', 'lion', 'monkey', 'orange', 'pig', 'rabbit', 'sheep', 'tiger', 'whale', 'zebra']
    
    word_count = {}
    
    for word in words:
        
        word_count[word] = word_count.get(word, 0) + 1
    
    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in word_count_sorted:
        
        print(word, count)
    
