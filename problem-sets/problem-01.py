def number_of_vowels(string):
    '''
    string: a string
    returns: number of vowels contained in the string
    '''
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count = count + 1
    return count

print('Number of vowels:', number_of_vowels('Hola mundo'))

