#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its content
    while True:
        numbers.append(int(input("Enter a number: ")))
        #A while loop that prints out the contents of numbers.txt every second
        time.sleep(1)
        #A for loop that prints out each number in numbers.txt every second
        for number in numbers:
            print(number)

