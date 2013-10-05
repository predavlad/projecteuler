s = raw_input()
while s:
    amount, balance = s.split(' ')
    amount, balance = int(amount), float(balance)

    if amount % 5 != 0 or amount <= 0:
        final_balance = balance
    elif balance - 0.5 < amount:
        final_balance = balance
    else:
        final_balance = balance - amount - 0.5

    print "%.2f" % final_balance
    s = raw_input()
