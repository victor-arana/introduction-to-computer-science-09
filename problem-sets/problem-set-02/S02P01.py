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
        
balance = 4842
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04

for i in range(1,13):
    print('Month: ', i) 
    print('Minimum monthly payment:', "%.2f" % minimumPayment(balance, monthlyPaymentRate, annualInterestRate, i))
    print('Remaining balance:', "%.2f" % remainingBalance(balance, monthlyPaymentRate, annualInterestRate, i))  
print('Total paid:', "%.2f" % totalPaid(balance, monthlyPaymentRate, annualInterestRate, 12))      
print('Remaining balance:', "%.2f" % remainingBalance(balance, monthlyPaymentRate, annualInterestRate, 12))
