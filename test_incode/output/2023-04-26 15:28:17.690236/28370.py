#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words and removes a list of numbers. """    
    
    removeWords(["a", "b", "c"], ["1", "2", "3"])
    removeWords(["a", "b", "c"], ["1", "2", "3"], True)
    removeWords(["a", "b", "c"], ["1", "2", "3"], False)
    
    removeNumbers(["1", "2", "3"], ["a", "b", "c"])
    removeNumbers(["1", "2", "3"], ["a", "b", "c"], True)
    removeNumbers(["1", "2", "3"], ["a", "b", "c"], False)
    
    removeWordsAndNumbers(["a", "b", "c"], ["1", "2", "3"])
    removeWordsAndNumbers(["a", "b", "c"], ["1", "2", "3"], True)
    removeWordsAndNumbers(["a", "b", "c"], ["1", "2", "3"], False)
    
    removeWordsAndNumbersAndWords(["a", "b", "c"], ["1", "2", "3"])
    removeWordsAndNumbersAndWords(["a", "b", "c"], ["1", "2", "3"], True)
    removeWordsAndNumbersAndWords(["a", "b", "c"], ["1", "2", "3"], False)
    
    removeWordsAndNumbersAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"])
    removeWordsAndNumbersAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], True)
    removeWordsAndNumbersAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], False)
    
    removeWordsAndNumbersAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], ["a", "b", "c"])
    removeWordsAndNumbersAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], ["a", "b", "c"], True)
    removeWordsAndNumbersAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], ["a", "b", "c"], False)
    
    removeWordsAndNumbersAndWordsAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"])
    removeWordsAndNumbersAndWordsAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], ["a", "b", "c"], ["a", "b", "c"], True)
    removeWordsAndNumbersAndWordsAndWordsAndWordsAndWords(["a", "b", "c"], ["1", "2", "3"], ["a", "b", "c"], 