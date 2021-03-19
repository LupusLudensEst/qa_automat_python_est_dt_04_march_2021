#1
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list) # What does it do? Think it is excessive string of code.
L.remove(L[5])
L.remove(L[4])
L.remove(L[0])
print(f'List after removing 0th, 4th, and 5th elements {L}')
print('*****************************')
#2
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Printed list except the first 5 elements {L[6:]}') # Your output is: [6, 7, 8, 9], thus there are left 6, not 5 elements: 0, 1, 2, 3, 4, 5
print('*****************************')
#3
a = 15
b = 6
print(f'Sum of 15 and 5 is {a + b}') # Mistake in the string: "Sum of 15 and 5 is" = 20- could be 21(15 + 6)
print(f'Absolute number of substruction of those numbers is {abs(a - b)}') # Why and what for did you use abs method?
print(f'Multiplication of those numbers is {a * b}')
print(f'Division of those numbers is {a / b}')
print('*****************************')
#4
a = '15'
b = 5
print(f'Multiplication of string and integer looks like this: {a * b}')
print(f'The result of multiplication of those numbers is {int(a) * b}')
print((f'If we need to print out "a + some words + b", we need to use b as a string.\n' +
       str(a) + ' is three times greater than ' + str(b)) * 10) # Why did you use combination of f''-formatted string and concatenation? Output is quite strange.
print('*****************************')
#5
num = [23, 568, -345, 0, 456, 3, -1]
print('Maximum number in this list is ' + str(max(num))) # Ok. But in the output we got string-not number(int or float).
print('Minimum number in this list is ' + str(min(num)))
print('*****************************')
#6
list = ['b', 'n', 'A', 'g', 'S', 'p', 'm' 'r', 'R', 'X', 'x', 'B' 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', '1', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
list.sort(reverse=True) # Interesting solution)))
print(list)

print('*****************************')

# May be it is worth to work with the code to make output more readable and informative.