def number_of_vowels(string):
    '''
    string: a string
    returns: number of vowels contained in the string
    '''
    return len([2 for letter in string if letter in 'aeiou']) 

s = 'Hola mundo'
print('Number of vowels:', number_of_vowels(s))

