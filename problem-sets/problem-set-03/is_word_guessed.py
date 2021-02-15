def readCSV(file_path, delim):
     import csv
     rows = []
     with open(file_path) as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=delim)
         for row in csv_reader:
             col = []
             for column in row:
                 col.append(str(column))
             rows.append(col)
     return rows

def is_word_guessed_test():
    separator = ','
    test_cases = readCSV('is_word_guessed_test_cases.csv',',')
    print('status', 'expected', 'actual', 'word', 'letters', sep=separator)
    for t in test_cases:
        status = 'FAILURE'
        expected = bool(t[0])
        word = t[1]
        letters = t[2]
        actual = isWordGuessed(word, letters)
        if actual == expected:
            status = 'success'
        else:
            status = 'FAILURE'
        print(status, expected, actual, word, letters, sep=separator)

          

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return secretWord in lettersGuessed 

is_word_guessed_test()

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
