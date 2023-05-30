#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and prints every number in it.
    while True:
        numbers = []
        with open('numbers.txt', 'r') as file:
            for line in file:
                numbers.append(int(line))
        print(numbers)
        
        

