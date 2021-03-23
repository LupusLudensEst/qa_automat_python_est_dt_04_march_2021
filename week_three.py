# if 'r' in ['a', 'b', 4]:
#     print('Its true')
# elif 4 in ['a', 'b', 4]:
#     print('we\'re in elif')
# else:
#     print('Its false')

# fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
# for fruit in fruits:
#     if fruit == 'Banana':
#         print('I hate bananas')
#     print(f'We have: {fruit}')

# fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
# for i in range(0, len(fruits)):
#     print(fruits[i])
#     if fruits[i] == 'Banana':
#         break

# fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
# for i in range(0, len(fruits)):
#     if fruits[i] == 'Banana':
#         continue
#     else:
#         print(fruits[i])


# fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
# for i in range(0, len(fruits)):
#     if fruits[i] == 'Banana':
#         pass
#     else:
#         print(fruits[i])

a, b, c, d = 5, 10, 3, 7
# def name_for_the_sum(num1: int = 77, num2: int = 3):
#     sum1 = int(num1) + int(num2)
#     print(sum1)
#
# name_for_the_sum(a, b)
# name_for_the_sum(a, c)
# name_for_the_sum(d, c)
# name_for_the_sum('3', '333')

# def name_for_the_sum(*args):
#     print(int(args[0]) + int(args[1]))
#
# name_for_the_sum(a, b)
# name_for_the_sum(a, c)
# name_for_the_sum(d, c)
# name_for_the_sum('3', '334')

# def name_for_the_sum(num1: str, num2: int = 3):
#     sum = int(num1) + int(num2)
#     return sum
#
# print(name_for_the_sum(a, b))
# print(name_for_the_sum(a, c))
# print(name_for_the_sum(d, c))
# print(name_for_the_sum('3', '334'))

class Car:
    """
    Documentation for cars
    """
    wheels = 4
    doors = 4

    def __init__(self, color):
        self.color = color

    def print_wheels(self):
        # print(self.wheels)
        return self.wheels, self.color

    def print_color(self):
        # print(self.color)
        return self.color

honda = Car(color='red')
honda.wheels = 10
# honda.print_wheels()
print(honda.print_wheels())
wheels, color = honda.print_wheels()
print(f'Wheels: {wheels}, color: {color}')
# honda.print_color()
a = {'adf': 'The value', 1: {'d', 'a'}}
print(a['adf'], ';', a[1])
print(honda.print_color())

toyota = Car(color='blue')
toyota.wheels = 8
# toyota.print_wheels()
print(toyota.print_wheels())
# toyota.print_color()
print(toyota.print_color())
print(dir(1))
print(type(1))

'string'.upper().format().lower()




