"'#input balance'"
def payingdebtoffinayear(balance, annual_interest_rate, monthly_payment_rate):
    '''
    function def
    '''
    month = 1
    while month <= 12:
        monthly_interest_rate = (annual_interest_rate) / 12.0
        minimum_monthly_payment = (monthly_payment_rate) * (balance)
        monthly_unpaid_balance = (balance) - (minimum_monthly_payment)
        updated_balance = (monthly_unpaid_balance) +\
                          (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance
        month += 1
    return round(updated_balance, 2)
def main():
    '''
    call
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: "+str(payingdebtoffinayear(data[0], data[1], data[2])))

if __name__ == "__main__":
    main()
