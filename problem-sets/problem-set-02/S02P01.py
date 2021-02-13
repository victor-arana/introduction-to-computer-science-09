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


def remaining_balance_test():
    test_cases = readCSV('S02P01-test-cases.csv',',')
    separator = ','
    print('status', 'expected', 'actual', 'balance', 'annualInterestRate', 'monthlyPaymentRate', sep=separator)
    for t in test_cases:
        status = 'FAILURE'
        expected = t[0]
        balance = t[1]
        annualInterestRate = t[2]
        monthlyPaymentRate = t[3]
        actual = remainingBalance(balance, monthlyPaymentRate, annualInterestRate, 12)
        actual = round(actual,2)
        if actual == expected:
            status = 'success'
        else:
            status = 'FAILURE'
            print(status, expected, actual, balance, annualInterestRate, monthlyPaymentRate, sep=separator)
        

def remainingBalance(b_0, r_m, r_a, i):
    '''
    b_0: Initial balance
    r_m: Minimum monthly payment rate
    r_a: Annual Interest rate
    i: Month
    ''' 
    if i > 0:
        return remainingBalance(b_0, r_m, r_a, i-1)*(1-r_m)*(1+r_a/12.0)
    else:
        return b_0
        
def minimumPayment(b_0, r_m, r_a, i):
    '''
    b_0: Initial balance
    r_m: Minimum monthly payment rate
    r_a: Annual Interest rate
    i: Month
    ''' 
    return remainingBalance(balance, monthlyPaymentRate, annualInterestRate, i-1)*r_m

def totalPaid(b_0, r_m, r_a, i):
    '''
    b_0: Initial balance
    r_m: Minimum monthly payment rate
    r_a: Annual Interest rate
    i: Month
    ''' 
    total = 0
    for j in range(1, i+1):
        total += minimumPayment(b_0, r_m, r_a, j)
    return total

#remaining_balance_test()

balance = 42
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04

print('Remaining balance:', round(remainingBalance(balance, monthlyPaymentRate, annualInterestRate, 12), 2))
