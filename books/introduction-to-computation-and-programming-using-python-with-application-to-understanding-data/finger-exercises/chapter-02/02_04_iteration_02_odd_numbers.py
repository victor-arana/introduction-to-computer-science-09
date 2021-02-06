# Write a program that asks the user to input 10 integers, and then
# print the largest odd number that was entered. If no odd number
# was entered, it should print a message to that effect.

def largest_odd_number_test():
    # 0: expected value
    # 1-3: arguments
    test_cases = []
    test_cases.append([5,1,3,5]) 
    test_cases.append([5,5,1,3]) 
    test_cases.append([5,3,5,1])
    test_cases.append(['No odd numbers', 2, 4, 6])
    for t in test_cases:
        actual = largest_odd_number(t[1],t[2],t[3])
        expected = t[0]
        if actual == expected: 
            print('pass', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )
        else:
            print('fail', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )

def filter_odd_numbers(numbers):
    odd_numbers = []
    for n in numbers:
        if n % 2 != 0:
            odd_numbers.append(n)
    return odd_numbers

def max_number(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n >= max_num:
            max_num = n
    return max_num

def largest_odd_number(x, y, z):
    '''
    x: integer number
    y: integer number
    z: integer number
    return: largest odd number among x, y, and z. If none are 
            odd print a message to that effect
    '''
    largest_odd_number = None
    numbers = [x, y, z]
    odd_numbers = filter_odd_numbers(numbers)
    if len(odd_numbers) > 0:
        return max_number(odd_numbers)
    else: 
        return 'No odd numbers' 

largest_odd_number_test()
integers_string = input('Enter 10 integers separated by space:')
integers_string_list = integers_string_list.split()
integers_list = []
for i in integers_string_list:
    integers_list.append(int(i))



