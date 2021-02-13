def readCSV(file_path, delim):
    import csv
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        for row in csv_reader:
            col = []
            for column in row:
                col.append(float(column))
            rows.append(col)
    return rows

def remainingBalance(b_0, p_f, r_a, i):
    '''
    b_0: Initial balance
    p_f: Fixed payment
    r_a: Annual Interest rate
    i: Month
    '''
    if i > 0:
        return remainingBalance(b_0, p_f, r_a, i-1)*(1+r_a/12.0) - p_f*(1+r_a/12.0)
    else:
        return b_0

def minimumPayment(balance, annualInterestRate, fixedMonthlyPayment, months):
    while remainingBalance(balance, fixedMonthlyPayment, annualInterestRate, months) >= 0:
        fixedMonthlyPayment = fixedMonthlyPayment + 10
    return fixedMonthlyPayment

def minimum_payment_test():
    test_cases = readCSV('S02P02-test-cases.csv',',')
    separator = ','
    print('status', 'expected', 'actual', 'balance', 'annualInterestRate', sep=separator)
    for t in test_cases:
        status = 'FAILURE'
        expected = t[0]
        balance = t[1]
        annualInterestRate = t[2]
        actual = minimumPayment(balance, annualInterestRate, 10, 12)
        actual = round(actual,2)
        if actual == expected:
            status = 'success'
        else:
            status = 'FAILURE'
        print(status, expected, actual, balance, annualInterestRate, sep=separator)


#Calculates the minimum fixed monthly payment needed in order pay off 
#a credit card balance within 12 months

minimum_payment_test()

balance = 3926
annualInterestRate = 0.2 
fixedMonthlyPayment = 10
months = 12

print('Lowest Payment:', minimumPayment(balance, annualInterestRate, fixedMonthlyPayment, months))
