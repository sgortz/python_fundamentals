# Write the following Python code to do the following (complete ALL of these using list comprehension).

# 1. Given a list [1,2,3,4], print out all the values in the list.
list_1 = [1, 2, 3, 4]
for val in list_1:
    print(val)

print('---1---')
# 2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
for val in list_1:
    print(val * 20)

print('---2---')
# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
list_2 = ["Elie", "Tim", "Matt"]
first_letter = []

for val in list_2:
    first_letter.append(val[0])

print(first_letter)
print('---3---')
# 4. Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
list_3 = [1, 2, 3, 4, 5, 6]
even_list_3 = []

for num in list_3:
    if num % 2 == 0:
        even_list_3.append(num)

print(even_list_3)
print('---4---')
# 5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
intersection = [num for num in list_1 if num in [3, 4, 5, 6]]
print(intersection)
print('---5---')
# 6. Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word
# reversed and in lower case (['eile', 'mit', 'ttam']).
new_list = []
for name in list_2:
    new_list.append(name.lower()[::-1])
print(new_list)
print('---6---')
# 7. Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).

print('---7---')
# 8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
divisible_by_12 = [num for num in range(1, 100) if num % 12 == 0]
print(divisible_by_12)
print('---8---')
# 9. Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
vowels_removed = [char for char in "amazing" if char not in ['a','e','i','o','u']]
print(vowels_removed)
print('---9---')
# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
output, i = [], 0
while i < 3:
    output.append([num for num in range(0,3)])
    i+=1
print(output)    
print('---10---')
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
output_2, i = [], 0
while i < 10:
    output_2.append([num for num in range(0,10)])
    i+=1
print(output_2)   
print('---11---')
