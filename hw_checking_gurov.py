#
x = ["apple", "banana", "cherry"]
y = x # value of list_of_strings assigned/назначено to variable "y"
print(x is y) # output True because "y" just has value of list_of_strings
print(f'x: {x}, y: {y}')

y = ["apple", "banana", "cherry"]
y == x # there is a comparison,thus "y" is not equal to "x", "y" and "x" are different objects
print(x is y)
print(f'x: {x}, y: {y}')








