#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python store.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    store = Store()
    
    for word in words:
        store.add(word)
    
    print("Stored %d words in store" % len(store.words))
    
    print("\nWords:")
    for word in store.words:
        print(word)
    
    print("\nWords with punctuation:")
    for word in store.words_with_punctuation:
        print(word)
    
    print("\nWords with numbers:")
    for word in store.words_with_numbers:
        print(word)
    
    print("\nWords with special characters:")
    for word in store.words_with_special_characters:
        print(word)
    
    print("\nWords with special characters and numbers:")
    for word in store.words_with_special_characters_and_numbers:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters and numbers:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters_and_numbers:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters and numbers and punctuation:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters_and_numbers_and_punctuation:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters and numbers and punctuation and special characters:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters_and_numbers_and_punctuation_special_characters_and_special_characters:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters and numbers and punctuation and special characters and numbers:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters_and_numbers_and_punctuation_special_characters_and_special_characters_and_numbers_and_punctuation:
        print(word)
    
    print("\nWords with special characters and numbers and punctuation and special characters and numbers and punctuation and special characters and numbers and punctuation:")
    for word in store.words_with_special_characters_and_numbers_and_punctuation_special_characters_and_numbers_and_punctuation_special_characters_and_special_characters_and_numbers_and_punctuation_special_characters_and_numbers_and_punctuation:
        print(word)
