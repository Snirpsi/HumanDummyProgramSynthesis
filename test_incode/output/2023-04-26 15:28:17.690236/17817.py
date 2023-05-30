#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input or adds words. """    
    
    # Get the input from the user
    word = input('Enter a word: ')
    
    # Check if the word is empty
    if not word:
        print('No word entered.')
    else:
        # Check if the word is lowercase
        if word.lower() == word:
            print('The word is already lowercase.')
        else:
            # Check if the word is uppercase
            if word.upper() == word:
                print('The word is already uppercase.')
            else:
                # Check if the word is capitalized
                if word.capitalize() == word:
                    print('The word is already capitalized.')
                else:
                    # Check if the word is converted to lowercase
                    if word.lower() != word:
                        print('The word is already lowercase.')
                    else:
                        # Check if the word is converted to uppercase
                        if word.upper() != word:
                            print('The word is already uppercase.')
                        else:
                            # Check if the word is converted to capitalized
                            if word.capitalize() != word:
                                print('The word is already capitalized.')
                            else:
                                # Check if the word is converted to all lowercase
                                if word.lower() != word.lower():
                                    print('The word is already lowercase.')
                                else:
                                    # Check if the word is converted to all uppercase
                                    if word.upper() != word.upper():
                                        print('The word is already uppercase.')
                                    else:
                                        # Check if the word is converted to all capitalized
                                        if word.capitalize() != word.capitalize():
                                            print('The word is already capitalized.')
                                        else:
                                            # Check if the word is converted to all lowercase
                                            if word.lower() != word.lower():
                                                print('The word is already lowercase.')
                                            else:
                                                # Check if the word is converted to all uppercase
                                                if word.upper() != word.upper():
                                                    print('The word is already uppercase.')
                                                else:
                                                    # Check if the word is converted to all capitalized
                                                    if word.capitalize() != word.capitalize():
                                                        print('The word is already capitalized.')
                                                    else:
                                                        # Check if the word is converted to all lowercase
                                                        if word.lower() != word.lower():
                                                            print('The word is already lowercase.')
                                                        else:
                                                            # Check if the word is converted to all uppercase
                                                            if word.upper() != word.upper():
                                                                print('The word is already uppercase.')
                                                            else:
                                                                # Check if the word is converted to all capitalized
                                                                if word.capitalize() != word.capitalize():
                                                                    print('The word is already capitalized.')
                                                else:
                                                    # Check if the word is converted to all lowercase
                                                    if word.lower() != word.lower():
                                                        print('The word is already lowercase.')
                                                else:
                                                    # Check if the word is converted to all uppercase
                                                    if word.upper() != word.upper():
                                                        print('The word is already uppercase.')
                                                else:
                                                    # Check if the word is converted to 