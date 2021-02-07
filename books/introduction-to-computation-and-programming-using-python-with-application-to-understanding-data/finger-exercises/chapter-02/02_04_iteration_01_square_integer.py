def square_int(x):
    '''
    Square an integer, the hard way
    x: integer number
    returns: x^2 x squared
    '''
    ans = 0
    itersLeft = x
    while (itersLeft != 0):
        ans = ans + x
        itersLeft = itersLeft - 1
    return ans

x = 3
print('x^2 =', square_int(x))
