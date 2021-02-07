# Write a program that asks the user to input 10 integers, and then
# print the largest odd number that was entered. If no odd number
# was entered, it should print a message to that effect.

def largest_odd_number_test():
    # 0: expected value
    # 1-3: arguments
    test_cases = readCSV('02_04_iteration_02_odd_numbers-test-cases.csv', ',', 'int')
    print('result','expected','actual','arguments', sep = ',')
    for t in test_cases:
        expected = t[0]
        arguments = t[1:]
        actual = largest_odd_number(arguments)
        result = 'FAILURE'
        if actual == expected:
            result = 'success'
        print(result, expected, actual, arguments, sep = ',')

def readCSV(file_path, delim, elements_type):
    '''
    Reads a csv file
    file_path: path to the file
    delim: delimiter used in the csv file
    elements_type: type of the elements to be returned
    return: a list containing elements of the specified type
    '''
    import csv
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        for row in csv_reader:
            col = []
            for column in row:
                if elements_type == 'float':
                    col.append(float(column))
                elif elements_type == 'int':
                    col.append(int(column))
            rows.append(col)
    return rows


def filter_odd_numbers(numbers):
    odd_numbers = []
    for n in numbers:
        if n % 2 != 0:
            odd_numbers.append(n)
    return odd_numbers

def max_number(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n >= max_num:
            max_num = n
    return max_num

def largest_odd_number(integers_list):
    '''
    integers_list: list of integers
    return: largest odd number in the list. If none are 
            odd print a message to that effect
    '''
    largest_odd_number = 'No odd numbers'
    odd_numbers = filter_odd_numbers(integers_list)
    if len(odd_numbers) > 0:
        largest_odd_number = max_number(odd_numbers) 
    return largest_odd_number

largest_odd_number_test()
integers_string = input('Enter 10 integers separated by space: ')
integers_string_list = integers_string.split()
integers_list = []
for i in integers_string_list:
    integers_list.append(int(i))

print('largest odd number:', largest_odd_number(integers_list))
