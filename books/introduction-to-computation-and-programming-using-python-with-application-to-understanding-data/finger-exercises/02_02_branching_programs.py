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
    return x

def largest_odd_number_test():
    x = 1
    y = 3
    z = 5
    if z == largest_odd_number(x,y,z):
        print('pass')
    else:
        print('fail')

largest_odd_number_test()
