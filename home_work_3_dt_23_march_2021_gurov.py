print(f"hw_3_classes_if_for_dt_23_march_2021\n1. Write function for list of integers (create own) which returns list but with each element's index added to the itself.\n"
      f"E.g function_name([0, 1, 3, 5]) => [0, 2, 5, 8]")
def ndx_ddd_itslf(m_lst):
    for i, x in enumerate(m_lst):
        print(f'Index "{i}" + its value "{x}" = "{i + x}"')
print(ndx_ddd_itslf(list(range(-10, 10))))


print(f"""
2. Write function for list of elements (create own) that will return indices of all occurrences of that item in list
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'b') => [3, 4, 5]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 1) => [0, 6]
e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'c') => []
""")
def rtrn_indxs_of_ll_ccrncs(lst_2, trgt):
    counter = list()
    for i in list(range(0, len(lst_2))):
        if lst_2[i] == trgt:
            counter.append(i)
    return counter
print(f"""
1. {rtrn_indxs_of_ll_ccrncs([ 1, 2, 4, 'b', 'b', 'b', 1], 'b')}
2. {rtrn_indxs_of_ll_ccrncs([ 1, 2, 4, 'b', 'b', 'b', 1], 1)}
3. {rtrn_indxs_of_ll_ccrncs([ 1, 2, 4, 'b', 'b', 'b', 1], 'c')}
""")


print("""
3. Create a function that takes an integer and returns its length.
e.g. function_name(8) => 1
e.g. function_name(88) => 2
e.g. function_name(83894) => 5
(Can't use len())
""")
intgr = str(int(input("Enter the integer: ")))
def len_of_int(intgr):
    counter = 0
    for symbol in intgr:
        counter += 1
    return counter
print(f'Length of "{intgr}" is "{len_of_int(intgr)}"')


print("""
4. Write a function that inverts the keys and values of a dictionary.
# e.g. function_name({ 'a': 'b', 'c': 'd' }) => { 'b': 'a', 'd': 'c' }
# e.g. function_name({ 'fruit': 'apple', 'meat': 'beef' }) => { 'apple': 'fruit', 'beef': 'meat' }
""")
dctnry = { 'a': 'b', 'c': 'd' }
def ky_vl_invrtd(dctnry):
    result = dict([(vl, ky) for ky, vl in dctnry.items()])
    return result

print(f"Input dictionary: {dctnry};\nOutput dictionary: {ky_vl_invrtd(dctnry)}")


print("""
5. Create class with attributes for last name and first name, full name and initials. 
Add functions to print full name, last name, first name, and initials
object_name = ClassName('john', 'DOE')
object_name.attribute_for_name => 'John Doe'
object_name.attribute_for_last_name => 'Doe'
object_name.attribute_for_first_name => 'John'
object_name.attribute_for_initials => 'J.D.'
object_name.print_full_name() => 'John Doe'
""")

class Client:
    """
    Documentation for ClassName
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.initials = initials

    def print_first_name(self):
        print(f'First name: {first_name.title()}')

    def print_last_name(self):
        print(f'Last name: {last_name.title()}')

    def print_full_name(self):
        print(f'Full name: {full_name.title()}')

    def print_initials(self):
        print(f'Initials: {initials}')

first_name = str(input("Enter the first name: "))
last_name = str(input("Enter the last name: "))
full_name = (f'{first_name} {last_name}')
initials = (f'{first_name[0].upper()}.{last_name[0].upper()}.')

object_1 = Client(first_name, last_name)
object_1.print_first_name()
object_1.print_last_name()
object_1.print_full_name()
object_1.print_initials()
