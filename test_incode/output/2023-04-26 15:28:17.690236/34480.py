#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or removes a list of words. """    
    
    numbers = input("Enter numbers: ")
    words = input("Enter words: ")
    
    numbers = numbers.split()
    words = words.split()
    
    numbers = [int(n) for n in numbers]
    words = [w.lower() for w in words]
    
    numbers = list(set(numbers))
    words = list(set(words))
    
    numbers.sort()
    words.sort()
    
    numbers = numbers[::-1]
    words = words[::-1]
    
    numbers = numbers[:10]
    words = words[:10]
    
    numbers = numbers + words
    
    numbers = " ".join(map(str, numbers))
    words = " ".join(map(str, words))
    
    print("Numbers:", numbers)
    print("Words:", words)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
