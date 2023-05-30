#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and multiplyes a list of numbers. """    
    
    words = []
    numbers = []
    
    for _ in range(int(input())):
        words.append(input())
        numbers.append(list(map(int, input().split())))
    
    words = list(set(words))
    numbers = list(set(numbers))
    
    words.sort()
    numbers.sort()
    
    words = [word for word in words if word in numbers]
    numbers = [number for number in numbers if number in words]
    
    words = [word for word in words if len(word) == 1]
    numbers = [number for number in numbers if len(number) == 1]
    
    words = list(set(words))
    numbers = list(set(numbers))
    
    words.sort()
    numbers.sort()
    
    print(" ".join(words))
    print(" ".join(numbers))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    