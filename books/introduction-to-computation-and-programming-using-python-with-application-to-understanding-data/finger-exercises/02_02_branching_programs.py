# Examines three variables x, y, and z and prints the largest
# odd number among them. If none of them are odd, it should
# print a message to that effect

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
        return None
    

def largest_odd_number_test():
    # 0: expected value
    # 1-3: arguments
    test_cases = []
    test_cases.append([5,1,3,5]) 
    test_cases.append([5,5,1,3]) 
    test_cases.append([5,3,5,1])
    for t in test_cases:
        actual = largest_odd_number(t[1],t[2],t[3])
        expected = t[0]
        if actual == expected: 
            print('pass', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )
        else:
            print('fail', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )

largest_odd_number_test()
