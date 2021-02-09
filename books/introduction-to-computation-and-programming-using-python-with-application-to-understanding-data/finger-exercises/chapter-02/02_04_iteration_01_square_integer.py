def square_int_test():
    test_cases = []
    test_cases.append([9, -3])
    test_cases.append([1, -1])
    test_cases.append([0, 0])
    test_cases.append([1, 1])
    test_cases.append([9, 3])
    status = 'FAILURE'
    print('status','expected','actual','argument', sep = ',')
    for t in test_cases:
        expected = t[0]
        argument = t[1]
        actual = square_int(argument)
        if expected == actual:
            status = 'success'
        print(status, expected, actual, argument, sep = ',')

def square_int(x):
    '''
    Square an integer, the hard way
    x: integer number
    returns: x^2 x squared
    '''
    ans = 0
    itersLeft = abs(x)
    while (itersLeft != 0):
        ans = ans + abs(x)
        itersLeft = itersLeft - 1
    return ans

square_int_test()
