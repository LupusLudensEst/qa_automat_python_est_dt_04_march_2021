print(f'Homework_2, Week 2, 17 March 2021.\n1. Write a Python program to print a specified list after removing the 0th, 4th, and 5th elements.')
list_1 = [1, 2, 3, 4, 'String', [5, 6, 7, 8], 'Alfa', 'Beta']
print(f'List_1 before removing with indexes: {list(enumerate(list_1))}')
del list_1[5]
print(f'List_1 after removing 5th element: {list_1}')
del list_1[4]
print(f'List_1 after removing 4th element: {list_1}')
del list_1[0]
print(f'List_1 after removing 0th element: {list_1}')
# 1.2
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# enumerated_list_1 = list(enumerate(list_1))
# print(enumerated_list_1)
# indexes_to_remove = [0, 4, 5]
# list_1 = [value for index, value in enumerate(list_1) if index not in indexes_to_remove]
# print(list_1)
# 1.3
# def delete_multiple_elements(list_object, indexes):
#     indexes = sorted(indexes, reverse=True)
#     for idx in indexes:
#         if idx < len(list_object):
#             list_object.pop(idx)
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# enumerated_list_1 = list(enumerate(list_1))
# list_of_indices = [0, 4, 5]
# # Remove elements from list_of_num at index 0, 4 and 5
# delete_multiple_elements(list_1, list_of_indices)
# print(f'{enumerated_list_1}\n{list_1}')
print('\n')

print(f'2. Write a Python program to generate and print a list except for the first 5 elements')
list_2 = [1, 2, 3, 4, 'String', [5, 6, 7, 8], 'Alfa', 'Beta']
print(f'List_2: {list_2}')
list_2_after_5th = list_2[5:]
print(f'List_2 print a list except for the first 5 elements: {list_2_after_5th}')
print('\n')

print(f'3. Write a Python program to assign a number to a and b and print the result of sum, subtraction, multiplication, division')
a = round(float(input("Enter the 1th number: ")), 2)
b = round(float(input("Enter the 1th number: ")), 2)
sum = round((a + b), 2)
subtraction = round((a - b), 2)
multiplication = round(a * b, 2)
division = round(a / b, 2)
print(f'Sum {a} + {b} = {sum}\nSubstraction {a} - {b} = {subtraction}\n'
      f'Multiplication {a} * {b} = {multiplication}\nDivision {a} / {b} = {division}')
print('\n')

print(f'4. Write a Python program to assign a number to either a or b and another should be a string '
      f'(you can decide which one is string and which one is integer or assume that they can be different type every run) '
      f'and print the result of the multiplication. Also, print change both to string '
      f'and print out “a + any word + b” 10 times where a and b are your values.')
# 1
a = int(input('Enter the integer: '))
b = str(input('Enter the string: '))
print(f'4.1. Type a: "{type(a)}\n'
      f'Type b: {type(b)}"')
# 2
multiplication = a * b
print(f'4.2. Multiplication: {a} * {b} = {multiplication}')
# 3
a = str(a)
print(f'4.3. Type a: "{type(a)}')
# 4
print(f'4.4. {a} any word {b}')
# 5
a_anyword_b = int(a) * (a + b + "\n")
print(f'4.5. {a} any word {b} * {int(a)} = {a_anyword_b}')
print('\n')

print(f'5. Write a Python program to print a list of integers without minimum and maximum values')
list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 999, -888]
print(f'List_5 before printing without minimum and maximum values: {list_5}')
list_5.remove(min(list_5))
list_5.remove(max(list_5))
print(f'List_5 after printing without minimum and maximum values: {list_5}')
print('\n')

print(f"6. Write a Python program to sort and then print reverse list: ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']")
list_6 = ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
print(f'List_6 before sorting and reversing: {list_6}')
list_6.sort()
# list_6_sorted_reversed = list_6[::-1]
list_6.reverse()
# print(f'List_6 after sorting and reversing by [::-1]: {list_6_sorted_reversed}')
print(f'List_6 after sorting and reversing by "reverse": {list_6}')
print('\n')