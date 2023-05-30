#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or calculates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    numbers = calculate_numbers(words)
    
    print("Numbers:")
    for number in numbers:
        print(number)
        
    print("Words:")
    for word in words:
        print(word)
    
    print("Total:", sum(numbers))
    
    print("Average:", sum(numbers) / len(numbers))
    
    print("Word count:", len(words))
    
    print("Word frequency:", len(set(words)))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(words))
    
    print("Word frequency:", len(set(words))/len(