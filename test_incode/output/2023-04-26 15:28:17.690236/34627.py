#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and converts fruits. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        words.append(line)
    
    fruits = []
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        fruits.append(line)
    
    words.sort()
    fruits.sort()
    
    words = words[:10]
    fruits = fruits[:10]
    
    words = [word for word in words if word.isalpha()]
    fruits = [fruit for fruit in fruits if fruit.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    fruits = [fruit for fruit in fruits if len(fruit) > 1]
    
    words = [word for word in words if len(word) > 2]
    fruits = [fruit for fruit in fruits if len(fruit) > 2]
    
    words = [word for word in words if len(word) > 3]
    fruits = [fruit for fruit in fruits if len(fruit) > 3]
    
    words = [word for word in words if len(word) > 4]
    fruits = [fruit for fruit in fruits if len(fruit) > 4]
    
    words = [word for word in words if len(word) > 5]
    fruits = [fruit for fruit in fruits if len(fruit) > 5]
    
    words = [word for word in words if len(word) > 6]
    fruits = [fruit for fruit in fruits if len(fruit) > 6]
    
    words = [word for word in words if len(word) > 7]
    fruits = [fruit for fruit in fruits if len(fruit) > 7]
    
    words = [word for word in words if len(word) > 8]
    fruits = [fruit for fruit in fruits if len(fruit) > 8]
    
    words = [word for word in words if len(word) > 9]
    fruits = [fruit for fruit in fruits if len(fruit) > 9]
    
    words = [word for word in words if len(word) > 10]
    fruits = [fruit for fruit in fruits if len(fruit) > 10]
    
    words = [word for word in words if len(word) > 11]
    fruits = [fruit for fruit in fruits if len(fruit) > 11]
    
    words = [word for word in words if len(word) > 12]
    fruits = [fruit for fruit in fruits if len(fruit) > 12]
    
    words = [word for word in words if len(word) > 13]
    fruits = [fruit for fruit in fruits if len(fruit) > 13]
    
    words = [word for word in 