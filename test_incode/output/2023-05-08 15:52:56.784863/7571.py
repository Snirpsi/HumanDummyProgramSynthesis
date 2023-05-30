#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its content
    while True:
        file = open("numbers.txt", "r")
        numbers = file.readlines()
        file.close()
        print(numbers)
        
        
        

