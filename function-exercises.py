# Write the following functions

# 1. difference - this function takes in two parameters and returns the difference between the two
def difference(a, b):
    return a - b


exercise_1_1 = difference(2, 2)  # 0
exercise_1_2 = difference(0, 2)  # -2
print('Should print 0: ', exercise_1_1)
print('Should print -2: ', exercise_1_2)

# 2. product - this function takes in two parameters and returns the product of the two
def product(a, b):
    return a * b


exercise_2_1 = product(2, 2)  # 4
exercise_2_2 = product(0, 2)  # 0
print('Should print 4: ', exercise_2_1)
print('Should print 0: ', exercise_2_2)

# 3. print_day - this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday,
# 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None
def print_day(num):
    if 1 > num or num > 7:
        return None
    else:
        weekdays = ['Sunday', 'Monday', 'Tuesday',
                    'Wednesday', 'Thursday', 'Friday', 'Saturday']
        return weekdays[num - 1]


exercise_3_1 = print_day(4)  # "Wednesday"
exercise_3_2 = print_day(41)  # None

print('Should print Wednesday: ', exercise_3_1)
print('Should print None: ', exercise_3_2)

# 4. last_element - this function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.
def last_element(list):
    if len(list) == 0:
        return None
    else:
        return list[len(list) - 1]


exercise_4_1 = last_element([1, 2, 3, 4])  # 4
exercise_4_2 = last_element([])  # None

print('Should print 4: ', exercise_4_1)
print('Should print None: ', exercise_4_2)

# 5. number_compare - this function takes in two parameters (both numbers). If the first is greater than the second, this function returns
# "First is greater." If the second number is greater than the first, the function returns "Second is greater." Otherwise the function returns
# "Numbers are equal."
def number_compare(num_1, num_2):
    if num_1 > num_2:
        return "First is greater"
    elif num_2 > num_1:
        return "Second is greater"
    else:
        return "Numbers are equal"


exercise_5_1 = number_compare(1, 1)  # "Numbers are equal"
exercise_5_2 = number_compare(1, 2)  # "Second is greater"
exercise_5_3 = number_compare(2, 1)  # "First is greater"

print('Should print "Numbers are equal": ', exercise_5_1)
print('Should print "Second is greater": ', exercise_5_2)
print('Should print "First is greater": ', exercise_5_3)

# 6. single_letter_count - this function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter.
# The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is
# lowercase or uppercase). If the letter is not found in the word, the function should return 0.
def single_letter_count(word, letter):
    new_letter = letter.lower()
    count = 0
    for char in word:
        if char == new_letter:
            count += 1
    return count


exercise_6_1 = single_letter_count('amazing', 'A')  # 2
exercise_6_2 = single_letter_count('amazing', 'Z')  # 1
exercise_6_3 = single_letter_count('amazing', 'E')  # 0
print('Should print 2: ', exercise_6_1)
print('Should print 1: ', exercise_6_2)
print('Should print 0: ', exercise_6_3)

# 7. multiple_letter_count - this function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being
# the count of the letter.
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


exercise_7_1 = multiple_letter_count("hello")  # {h:1, e: 1, l: 2, o:1}
# {p:1, e: 1, r: 1, s:1, o:1, n:1}
exercise_7_2 = multiple_letter_count("person")

print('Should print h:1, e: 1, l: 2, o:1}: ', exercise_7_1)
print('Should print p:1, e: 1, r: 1, s:1, o:1, n:1}: ', exercise_7_2)

# 8. list_manipulation - this function should take in three parameters (a list, command, location and value).
# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list
def list_manipulation(lists, command, location, value=''):
    if command == 'remove':
        if location == 'end':
            popped = lists[len(lists) - 1]
            lists[1:]
            return popped
        elif location == 'beginning':
            value = lists[0]
            lists[0:1]
            return value
    elif command == 'add':
        if location == 'beginning':
            lists.insert(0, value)
            return lists
        elif location == 'end':
            lists.append(value)
            return lists


exercise_8_1 = list_manipulation([1, 2, 3], "remove", "end")  # 3
exercise_8_2 = list_manipulation([1, 2, 3], "remove", "beginning")  # 1
exercise_8_3 = list_manipulation([1, 2, 3], "add", "beginning", 20)  # [20,1,2,3]
exercise_8_4 = list_manipulation([1, 2, 3], "add", "end", 30)  # [1,2,3,30]

print('Should print 3: ', exercise_8_1)
print('Should print 1: ', exercise_8_2)
print('Should print [20, 1, 2, 3]: ', exercise_8_3)
print('Should print [1, 2, 3, 30]: ', exercise_8_4)

# 9. is_palindrome - A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
# This function should take in one parameter and returns True or False depending on whether it is a palindrome.
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.
def is_palindrome(param):
    new_list = list(param)
    middle_idx = abs(len(new_list) // 2)

    count = 0
    
    while count != middle_idx:
        # if list is even num length
        if len(new_list) % 2 == 0:
            # if first char from 1 half is the same as 1st char of second half
            if new_list[middle_idx - count] != new_list[middle_idx - (1 - count)]:

                return False
        else:
            if new_list[middle_idx - count] != new_list[middle_idx + count]:
                return False   
        count += 1
    return True

exercise_9_1 = is_palindrome('testing')  # False
exercise_9_2 = is_palindrome('tacocat')  # True
exercise_9_3 = is_palindrome('hannah')  # True
exercise_9_4 = is_palindrome('robert')  # False

print('Should be False: ', exercise_9_1)
print('Should be True: ', exercise_9_2)
print('Should be True: ', exercise_9_3)
print('Should be False: ', exercise_9_4)

# 10. frequency - This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.
def frequency(lists, term):
    return lists.count(term)

exercise_10_1 = frequency([1, 2, 3, 4, 4, 4], 4)  # 3
exercise_10_2 = frequency([True, False, True, True], False)  # 1
print('Should print 3: ', exercise_10_1)
print('Should print 1: ', exercise_10_2)

# 11. flip_case - This function accepts a string and a letter and reverses the case of all occurances of the letter in the string.
def flip_case(str, target_letter):
    new_list = list()
    # iterate through the list 
    for letter in str:
        #find letter
        if letter.lower() == target_letter.lower():
            letter = letter.swapcase()
        new_list.append(letter)
    return ''.join(new_list)

    # return ''.join([letter if letter.lower() == target_letter.lower(): letter.swapcase() else: letter for letter in str ])
    

exercise_11 = flip_case("Hardy har har", "h")  # "hardy Har Har"
print('#11 Should print "hardy Har Har"', exercise_11)

# 12. multiply_even_numbers - This function accepts a list of numbers and returns the product of all even numbers in the list.
def multiply_even_numbers(num_list):
    count = 1
    for num in num_list:
        if num % 2 == 0:
            count *= num
    return count

exercise_12 = multiply_even_numbers([2, 3, 4, 5, 6])  # 48
print('#12 Should print 48: ', exercise_12)

# 13. mode - This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.
def mode(num_list):
    max_num = num_list[0]
    count = num_list.count(num_list[0])
    
    #iterate thru the list
    for  num in num_list:
        # if count of another one is higher,
        if num_list.count(num) > count:
            # reassign the count variable
            count = num_list.count(num)
            # and the max_num
            max_num = num

    return max_num
    

exercise_13_1 = mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4])  # 4
exercise_13_2 = mode([2, 7, 1, 2, 3, 3, 7, 7, 5, 7, 4, 6, 4, 6, 7, 4])  # 4
print('Should print 4: ', exercise_13_1)
print('Should print 7: ', exercise_13_2)

# 14. capitalize - This function accepts a string and returns the same string with the first letter capitalized.
def capitalize(str):
    return str.capitalize()

exercise_14_1 = capitalize("tim")  # "Tim"
exercise_14_2 = capitalize("matt")  # "Matt"
print('#14 Should print "Tim": ', exercise_14_1)
print('#14 Should print "Matt": ', exercise_14_2)

# 15. compact - This function accepts a list and returns a list of values that are truthy values.
def compact(random_list):
    # make a copy of the list
    new_list = random_list.copy()
    # iterate over the list
    for value in new_list:
    #if falsy value, remove that item
        if bool(value) == False:
            new_list.remove(value)
    return new_list

exercise_15_1 = compact([0, 1, 2, "", [], False, {}, None, "All done"])  # [1,2, "All done"]
print('#15 Should print [1,2, "All done"]: ', exercise_15_1)

# 16. partition - This function accepts a list and a callback function (which you can assume returns True or False).
# The function should iterate over each element in the list and invoke the callback function at each iteration.
# If the result of the callback function is True, the element should go into one list if it's False, the element should go into another list.
# When it's finished, partition should return both lists inside of one larger list.
def is_even(num):
    return num % 2 == 0

def partition(num_list, cb):
    # create a list for falsy values and for truthy values inside the output list
    partitioned_nums = [[],[]]
    
    # iterate thru the list
    for num in num_list:
        # check each element for truthfulness
        if (cb(num)):
        # add in one list or another accordingly
            partitioned_nums[0].append(num)
        else:
            partitioned_nums[1].append(num)
    
    # return the main list
    return partitioned_nums


exercise_16 = partition([1, 2, 3, 4], is_even)  # [[2,4],[1,3]]
print('#16 Should print [[2,4],[1,3]]: ', exercise_16)

# 17. intersection - This function should accept a two dimensional list and return a list with the values that are the same in each list.
def intersection(num_list):
    


exercise_17 = intersection([[1, 2, 3], [2, 3, 4]])  # [2,3]
print('#17 Should print [2,3]: ', exercise_17)

# 18. once - This function accepts a function and returns a new function that can only be invoked once. If the function is invoked more than once,
# it should return None. Hint you will need to define a new function inside of your once function and return that function. You can add properties
# to your inner function to see if it has run already.


# def add(a, b):
#     return a + b


# one_addition = once(add)

# one_addition(2, 2)  # 4
# one_addition(2, 2)  # undefined
# one_addition(12, 200)  # undefined

# 19. Super bonus - Research what decorators are and refactor your once code to use a decorator so that you can run


# @run_once
# def add(a, b):
#     return a + b


# add(2, 2)  # 4
# add(2, 20)  # None
# add(12, 20)  # None