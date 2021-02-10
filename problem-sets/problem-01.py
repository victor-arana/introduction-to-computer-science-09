def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    return char in('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U')

count = 0
for char in s:
    if isVowel(char):
        count = count + 1
print('Number of vowels:', count)

