balance = 320000
annualInterestRate = 0.2

"""
Iteration version

max = (balance * ((1+(annualInterestRate/12))**12))/12
min = balance/12

while True:
    payment = (max-min)/2.0 + min
    balanceBuff = balance
    for month in range(1,13):
        balanceBuff = (balanceBuff-payment)+((annualInterestRate/12.0)*(balanceBuff-payment))
    if abs(balanceBuff) < 0.01:
        print("Lowest Payment: " + str(round(payment, 2)))
        break
    elif balanceBuff < 0.0:
        max = payment
    else:
        min = payment
        
"""

# Recursive Version

max = (balance * ((1+(annualInterestRate/12))**12))/12
min = balance/12

def intCheck(min, max, balance, rate):
    payment = (max-min)/2.0 + min
    balanceBuff = balance
    for month in range(1,13):
        balanceBuff = (balanceBuff-payment)+((annualInterestRate/12.0)*(balanceBuff-payment))
    if abs(balanceBuff) < 0.01:
        return str(round(payment, 2))
    elif balanceBuff < 0.0:
        return intCheck(min, payment, balance, rate)
    else:
        return intCheck(payment, max, balance, rate)

print("Lowest Payment: " + intCheck(min, max, balance, annualInterestRate))