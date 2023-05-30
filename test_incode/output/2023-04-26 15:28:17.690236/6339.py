#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: ./word.py <word>")
        exit(1)
    
    word = sys.argv[1]
    
    word_list = word.split()
    
    word_list_len = len(word_list)
    
    word_list_count = {}
    
    for i in range(word_list_len):
        word_list_count[word_list[i]] = word_list_count[word_list[i]] + 1
    
    word_list_count_sorted = sorted(word_list_count.items(), key=lambda x: x[1])
    
    print("Words sorted by count:")
    for word, count in word_list_count_sorted:
        print("\t", word, count)
    
    print("Words sorted by frequency:")
    for word, count in word_list_count_sorted:
        print("\t", word, count/word_list_len)
    
    print("Words sorted by length:")
    for word, count in word_list_count_sorted:
        print("\t", word, len(word))
    
    print("Words sorted by length in descending order:")
    for word, count in word_list_count_sorted:
        print("\t", word, count/word_list_len, end=" ")
    print()
    
    print("Words sorted by length in ascending order:")
    for word, count in word_list_count_sorted:
        print("\t", word, count/word_list_len, end=", ")
    print()
    
    print("Words sorted by length in reverse order:")
    for word, count in word_list_count_sorted:
        print("\t", word, count/word_list_len, end="")
    print()
    
    print("Words sorted by length in ascending order and in reverse order:")
    for word, count in word_list_count_sorted:
        print("\t", word, count/word_list_len, end=