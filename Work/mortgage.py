# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0
    principal = principal * (1+rate/12) - payment - extra
    total_paid = total_paid + payment + extra
    if principal < 0:
        total_paid += principal
        principal = 0
    
    # print(month, total_paid, principal)
        
print(f'Total paid {round(total_paid,2)}')
print(f'total months {month}')