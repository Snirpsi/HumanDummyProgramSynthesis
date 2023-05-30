#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or stores a list of numbers. """    
    
    # Read command line arguments
    words = []
    numbers = []
    
    # Read command line arguments
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    # Convert numbers to words
    if len(numbers) > 0:
        for number in numbers:
            words.append(str(number))
    
    # Convert words to numbers
    if len(words) > 0:
        for word in words:
            numbers.append(int(word))
    
    # Print results
    print("\n".join(str(number) for number in numbers))
    print("\n".join(str(word) for word in words))
    
    # Print number of words converted
    print("Number of words: " + str(len(words)))
    
    # Print number of numbers converted
    print("Number of numbers: " + str(len(numbers)))
    
    # Print the average number of numbers converted
    print("Average number of numbers: " + str(sum(numbers) / len(numbers)))
    
    # Print the average number of words converted
    print("Average number of words: " + str(sum(words) / len(words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / 3))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words) / len(numbers + words)))
    
    # Print the average number of numbers and words converted
    print("Average number of numbers and words: " + str(sum(numbers + words