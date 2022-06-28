# Write the following Python code to do the following (complete ALL of these using list comprehension).

# 1. Given a list [1,2,3,4], print out all the values in the list.
[print(val) for val in [1, 2, 3, 4]]

# 2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
[print(val * 20) for val in [1, 2, 3, 4]]

# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
first_letter = [name[0] for name in ["Elie", "Tim", "Matt"]]
print('#3: ', first_letter)

# 4. Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
even_list = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print('#4: ', even_list)

# 5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
intersection = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
print('#5: ', intersection)

# 6. Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word
# reversed and in lower case (['eile', 'mit', 'ttam']).
reversed_name = [name.lower()[::-1] for name in ["Elie", "Tim", "Matt"]]
print('#6: ', reversed_name)

# 7. Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).
string_intersection = ''.join([char for char in "first" if char in "third"])
print('#7: ', string_intersection)

# 8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
divisible_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print('#8: ', divisible_by_12)

# 9. Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
vowels_removed = [char for char in "amazing" if char not in [
    'a', 'e', 'i', 'o', 'u']]
print('#9: ', vowels_removed)

# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
output = [[num for num in range(0, 3)] for i in range(0, 3)]

# 11. Generate a list with the value:
# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
[[num for num in range(0, 10)] for i in range(0, 10)]