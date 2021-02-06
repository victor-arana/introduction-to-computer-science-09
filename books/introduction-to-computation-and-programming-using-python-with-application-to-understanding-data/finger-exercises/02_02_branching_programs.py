# Examines three variables x, y, and z and prints the largest
# odd number among them. If none of them are odd, it should
# print a message to that effect

def largest_odd_number(x, y, z):
    '''
    x: integer number
    y: integer number
    z: integer number
    return: largest odd number among x, y, and z. If none are 
            odd print a message to that effect
    '''
    largest_odd_number = None
    if z%2!=0:
        largest_odd_number = z
    return largest_odd_number

def largest_odd_number_test():
    # 0: expected value
    # 1-3: arguments
    test_cases = []
    test_cases.append([3,1,3,5]) 
    test_cases.append([3,5,1,3]) 
    test_cases.append([3,3,5,1])
    for t in test_cases:
        actual = largest_odd_number(t[1],t[2],t[3])
        expected = t[0]
        if actual == expected: 
            print('pass', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )
        else:
            print('fail', 'e:', expected, 'a:', actual, 'x:', t[1], 'y:', t[2], 'z:', t[3] )

largest_odd_number_test()
