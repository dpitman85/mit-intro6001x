balance = 3329
annualInterestRate = 0.2

payment = 10
balanceBuff = balance

while balanceBuff > 0:
    for month in range(1,13):
        balanceBuff = (balanceBuff-payment)+((annualInterestRate/12.0)*(balanceBuff-payment))
        print("Month {} Remaining balance: {}".format(str(month), str(round(balanceBuff, 2))))
    if balanceBuff <= 0:
        print("Lowest Payement: " + str(payment))
        break
    else:
        payment += 10
        balanceBuff = balance
        