def readCSV(file_path, delim):
    import csv
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        for row in csv_reader:
            col = []
            for column in row:
                col.append(column)
            rows.append(col)
    return rows

def problem_03_test():
    test_cases = readCSV('problem-03-test-cases.csv',',')
    separator = ','
    print('status', 'argument', 'actual', 'expected', sep=separator)
    for t in test_cases:
        argument = t[1]
        actual = longest_ordered(argument)
        expected = t[0]
        status = 'FAILURE'
        if actual == expected:
            status = 'success'
        print(status, argument, actual, expected, sep=separator)

def longest_ordered(string):
    return string

problem_03_test()
