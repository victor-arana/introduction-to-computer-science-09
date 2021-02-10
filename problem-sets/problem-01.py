def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char in('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')

def number_of_vowels(string):
    '''
    string: a string
    returns: number of vowels contained in the string
    '''
    count = 0
    for char in string:
        if isVowel(char):
            count = count + 1
    return count

print('Number of vowels:', number_of_vowels('Hola mundo'))

