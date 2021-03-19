# a = ''
# b = "Hello"
# c = 'And one more time \"Something in the doubled quotes\"\nNew line'
# if b == "Hello":
#     a = " "
# print(f'Hello {a} Vic')
# print(f'{b}, World')
# print(c)

# b = "Hello"
# print(b[0],'\n',b[::-1],'\n',len(b),'\n',b.upper(),'\n',b.lower())

# c = "Anything"
# d = "Something"
# space = " "
# new_str = "\n"
# print(f'C: {c}{space}D: {d}; {new_str}C: {c}{space}D: {d}')
# print(type(c), type(c), type([]))

# a = 1
# print(a)
# a += 2
# print(a)
# a -= 1
# print(a)

# a = "Hello!!!"
# print('o' in a, 'a' in a)
# print(type(a) is str, type(a) is not dict)

# a = 1
# if a == 1:
#     print('True')
# else:
#     print('False')

# a = 1
# b = 3
# if a == 1 and b == 3:
#     print('True')
# elif a == 1 and b != 1:
#     print('True again')
# else:
#     print('Nope')


# a = '1'
# b = 1
#
# print(type(b) is dict)
# if type(a) is float:
#     print(a * 3)
# else:
#     print(str(a) * 4)


# a = [6, 7, 8, 9]
# b  = [1, 2, 3, 4, 5, 'string1', a]
# print(len(b), [0], b[1], b[-1])
# print(b[::-1])
# b.append('Append')
# print(b)
# del(a[0])
# print(b)
# print(b * 3)
# print('string1' in b)
# print('string1' not in b)
# z = [1, 2, 3, 4, 5, 6, 7]
# print(max(z),'\n',min(z))
# print(b.count(1))
# print(b.index(1), b.index(a))

# list2 =[1, 2, 3, 4, -2, 10, 0, 0, 10]
# print(list2)
# print(list2.count(2))
# print(list2[0], list2[-1], list2[-2], list2[:-1], list2[len(list2)-1])
# a = list2.pop(list2[0])
# print(list2)
# print(''.join(reversed(str(list2))), list2[::-1])
# print(list2.sort())

# List [] - brackets, mutable
print("List []")
list_1 = [1, 2, 3, 4, 'String', [5, 6, 7, 8], 'Alfa']
print(f'1. Type of list_1: "{type(list_1)}"')
print(f'2. List list_1: "{list_1}, has "{len(list_1)}" members')
print(f'3. List list_1 can be reversed via slicing: {list_1[::-1]}')
list_1.append('Append')
print(f'4. To list can be added additional member: "{list_1}"')
print(f'5. 1th element of list a: "{list_1[0]}" and last element of list a: "{list_1[-1]}"')
for i in range(0, len(list_1)):
    print(f'#{i+1}: Element: "{list_1[i]}"')
    if 'a' in str(list_1[i]).lower():
        print(f'"a" in "{str(list_1[i])}"')
    else:
        print(f'"a" not in "{str(list_1[i])}"')
print('\n')

# Tuple/кортеж () - parentheses, immutable, used for locators keeping in Automation like: CONTACT_TEXT = (By.XPATH, "(//div[@class='review-block__content'])[1]")
print("Tuple/кортеж ()")
tuple_1 = (1, 2, 3, 4, "Tuple", [1, 2, 3], "Ulyana")
print(f'1. Type of tuple_1: "{type(tuple_1)}"')
# tuple_1.append('Append')
# print(f'2. Tuple is immutable: "{tuple_1}"') # AttributeError: 'tuple' object has no attribute 'append'
print(f'2. Tuple tuple_1 has length: "{len(tuple_1)}"')
print(f'3. Tuple tuple_1 can be reversed via slicing: "{tuple_1[::-1]}"')
for i in range(0, len(tuple_1)):
    print(f'#{i+1}: Element: "{tuple_1[i]}"')
    if 'u' in str(tuple_1[i]).lower():
        print(f'"u" in "{str(tuple_1[i])}"')
    else:
        print(f'"u" not in "{str(tuple_1[i])}"')
print('\n')

# Dictionary {} - braces
print("Dictionary {}")
dict_1 = {
    "key_0": "value_0",
    "key_1":"value_1",
    "key_2":"value_2",
    "key_3":"value_3",
    "key_4":"value_4",
}

print(f'1. Length of dictionary c: "{len(dict_1)}"')
print(f'2. Value of 1th key: "{dict_1["key_0"]:}", value of last key: "{dict_1["key_4"]:}"')
for key in dict_1:
    print(f'#{key}: Element: "{dict_1[key]}"')
    if 'u' in str(dict_1[key]):
        print(f'"u" in "{dict_1[key]}"')
    else:
        print(f'"u" not in "{dict_1[key]}"')
print('\n')

# Set {} is used to store multiple items in a single variable
print("Set {}")
set_1 = {"Uno", "Des", "Tres", "Argentum", "Para"}
print(f'1. Length of set_1 "{set_1}": "{len(set_1)}"')
print(f'2. Type of set_1: "{type(set_1)}"')
set_1_list = list(set_1)
print(f'3. Length of set_1_list "{set_1_list}": "{len(set_1_list)}"')
print(f'4. Type of set_1_list: "{type(set_1_list)}"')
print('\n')

# Boolean True/False
print("Boolean True/False")
bool_1 = "Hello!!!"
print('o' in bool_1, 'a' in bool_1)
print(type(bool_1) is str, type(bool_1) is not dict)

bool_2 = 1
bool_3 = 3
if bool_2 == 1 and bool_3 == 3:
    print('1. True')
elif bool_2 == 1 and bool_3 != 1:
    print('2. True again')
else:
    print('3. Nope')

list_1 = ['string_1', 'string_2', 'string_3']

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 10]
print(list_2)
b = list_2.index(2)
print(b)
a = list_2.pop(list_2[2]-1)
print(a)
print(list_2)