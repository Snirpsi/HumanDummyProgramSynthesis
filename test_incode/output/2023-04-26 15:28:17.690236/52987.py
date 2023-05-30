#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and calculates a list of words. """    
    numbers = []
    words = []
    while True:
        number = input("Enter a number: ")
        numbers.append(number)
        words.append(str(number))
        if number == "":
            break
    print("The numbers are:")
    print(numbers)
    print("The words are:")
    print(words)
    print("The sum of the numbers is " + str(sum(numbers)))
    print("The sum of the words is " + str(sum(words)))
    print("The average of the numbers is " + str(sum(numbers)/len(numbers)))
    print("The average of the words is " + str(sum(words)/len(words)))
    print("The difference of the numbers is " + str(sum(numbers)-sum(words)))
    print("The difference of the words is " + str(sum(words)-sum(numbers)))
    print("The difference of the sums is " + str(sum(numbers)-sum(words)))
    print("The difference of the averages is " + str(sum(numbers)/len(numbers)-sum(words)/len(words)))
    print("The difference of the averages is " + str(sum(words)/len(words)-sum(numbers)/len(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("The difference of the differences is " + str(sum(words)-sum(numbers)))
    print("The difference of the differences is " + str(sum(numbers)-sum(words)))
    print("