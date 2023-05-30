#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that requests numbers.
    #The function prints them out in reverse order.
    #The function also prints out the number of times each number appears.
    #The function also prints out the number of times each number appears twice.
    #The function also prints out the number of times each number appears three times.
    #The function also prints out the number of times each number appears four times.
    #The function also prints out the number of times each number appears five times.
    #The function also prints out the number of times each number appears six times.
    #The function also prints out the number of times each number appears seven times.
    #The function also prints out the number of times each number appears eight times.
    #The function also prints out the number of times each number appears nine times.
    #The function also prints out the number of times each number appears ten times.
    #The function also prints out the number of times each number appears eleven times.
    #The function also prints out the number of times each number appears twelve times.
    #The function also prints out the number of times each number appears thirteen times.
    #The function also prints out the number of times each number appears fourteen times.
    #The function also prints out the number of times each number appears fifteen times.
    #The function also prints out the number of times each number appears sixteen times.
    #The function also prints out the number of times each number appears seventeen times.
    #The function also prints out the number of times each number appears eighteen times.
    #The function also prints out the number of times each number appears nineteen times.
    #The function also prints out the number of times each number appears twenty times.
    #The function also prints out the number of times each number appears twenty times and then exits.
    numbers = range(1,11)
    numbers_count = Counter(numbers)
    numbers_count_dict = dict(numbers_count)
    numbers_count_dict_sorted = sorted(numbers_count.items(), key=operator.itemgetter(1), reverse=True)
    numbers_count_dict_sorted = [item for sublist in numbers_count_dict_sorted for item in sublist]
    print(numbers_count_dict_sorted)
    exit()

