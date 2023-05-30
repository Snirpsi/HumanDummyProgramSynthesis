#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    words = [w for w in sys.argv[1:] if w.strip()]
    
    word_count = len(words)
    
    word_count_dict = dict()
    
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    
    word_count_list = list(word_count_dict.values())
    
    word_count_list.sort(reverse=True)
    
    word_count_list.insert(0, 0)
    
    word_count_list.insert(0, word_count)
    
    word_count_list.insert(0, word_count_dict)
    
    word_count_list.insert(0, word_count_list)
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_count_list.insert(0, word_count_list[0])
    
    word_