#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and opens a list of words. """    
    
    words = []
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    
    print("\nWords:")
    for word in words:
        print(word)
    
    print("\nWords sorted:")
    
    words.sort()
    for word in words:
        print(word)
    
    print("\nWords reversed:")
    
    words.reverse()
    for word in words:
        print(word)
    
    print("\nWords shuffled:")
    
    words = list(words)
    random.shuffle(words)
    for word in words:
        print(word)
    
    print("\nWords shuffled reversed:")
    
    words = list(words)
    random.shuffle(words)
    words.reverse()
    for word in words:
        print(word)
    
    print("\nWords shuffled shuffled:")
    
    words = list(words)
    random.shuffle(words)
    words.shuffle()
    for word in words:
        print(word)
    
    print("\nWords shuffled shuffled reversed:")
    
    words = list(words)
    random.shuffle(words)
    words.shuffle()
    words.reverse()
    for word in words:
        print(word)
    
    print("\nWords shuffled shuffled shuffled reversed:")
    
    words = list(words)
    random.shuffle(words)
    words.shuffle()
    words.shuffle()
    words.reverse()
    for word in words:
        print(word)
    
    print("\nWords shuffled shuffled shuffled shuffled reversed:")
    
    words = list(words)
    random.shuffle(words)
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.reverse()
    for word in words:
        print(word)
    
    print("\nWords shuffled shuffled shuffled shuffled shuffled reversed:")
    
    words = list(words)
    random.shuffle(words)
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()
    words.shuffle()