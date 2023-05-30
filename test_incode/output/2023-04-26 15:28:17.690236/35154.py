#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    words = []
    
    # Read a text file and store each word in the list.
    with open('words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    # Print the list of words in alphabetical order.
    print(sorted(words))
    
    # Print the length of each word.
    print(len(words))
    
    # Print the average length of the words.
    print(sum(len(word) for word in words) / len(words))
    
    # Print the average length of the words in lowercase.
    print(sum(len(word.lower()) for word in words) / len(words))
    
    # Print the average length of the words in uppercase.
    print(sum(len(word.upper()) for word in words) / len(words))
    
    # Print the average length of the words in mixed case.
    print(sum(len(word.title()) for word in words) / len(words))
    
    # Print the average length of the words in mixed case with punctuation.
    print(sum(len(word) for word in words if word.isalpha()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase.
    print(sum(len(word) for word in words if word.isalpha() and word.islower()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase and uppercase.
    print(sum(len(word) for word in words if word.isalpha() and word.islower() and word.isupper()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase and uppercase and mixed case.
    print(sum(len(word) for word in words if word.isalpha() and word.islower() and word.isupper() and word.isalpha()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase and uppercase and mixed case with punctuation.
    print(sum(len(word) for word in words if word.isalpha() and word.islower() and word.isupper() and word.isalpha() and word.isdigit()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase and uppercase and mixed case with punctuation and lowercase and uppercase and mixed case.
    print(sum(len(word) for word in words if word.isalpha() and word.islower() and word.isupper() and word.isalpha() and word.isdigit() and word.isalnum()) / len(words))
    
    # Print the average length of the words in mixed case with punctuation and lowercase and uppercase and mixed case with punctuation and lowercase and uppercase and mixed case with punctuation and lowercase and uppercase and mixed case with punctuation and lowercase 