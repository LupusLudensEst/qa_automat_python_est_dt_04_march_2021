"""
Week 2, 17 March 2021
1. Write a Python program to print a specified list after removing the 0th, 4th, and 5th elements.
2. Write a Python program to generate and print a list except for the first 5 elements
3. Write a Python program to assign a number to a and b and print the result of sum, subtraction, multiplication, division
4. Write a Python program to assign a number to either a or b and another should be a string
(you can decide which one is string and which one is integer or assume that they can be different type every run)
and print the result of the multiplication. Also, print change both to string and print out “a + any word + b” 10 times where a and b are your values.
5. Write a Python program to print a list of integers without minimum and maximum values
6. Write a Python program to sort and then print reverse list: ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
"""

print(f'Homework_2, Week 2, 17 March 2021.\n1. Write a Python program to print a specified list after removing the 0th, 4th, and 5th elements.')
list_1 = [1, 2, 3, 4, 'String', [5, 6, 7, 8], 'Alfa', 'Beta']
print(f'List_1 before removing: {list_1}')
del list_1[0]
print(f'List_1 after removing 0th element: {list_1}')
del list_1[4]
print(f'List_1 after removing 4th element: {list_1}')
del list_1[5]
print(f'List_1 after removing 5th element: {list_1}')
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
sum = a + b
subtraction = a - b
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
print(f'4.2. Multiplication: int {a} * str {b} = str {multiplication}')
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