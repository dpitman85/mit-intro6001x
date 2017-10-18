balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    balance = (balance-(balance*monthlyPaymentRate))+((annualInterestRate/12.0)*(balance-(balance*monthlyPaymentRate)))
    print("Month {} Remaining balance: {}".format(str(month), str(round(balance, 2))))
    
print("Remaining balance: " + str(round(balance, 2)))