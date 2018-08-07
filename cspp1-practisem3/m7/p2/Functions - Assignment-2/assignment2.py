"'#input balance'"
def paying_debt_offina_year(balance, annual_interest_rate):
    '''
    function definition
    '''
    monthly_payment = 0
    bal = balance
    while bal > 0:
        bal = balance
        monthly_payment = monthly_payment + 10
        month = 1
        while month <= 12:
            monthly_interest_rate = (annual_interest_rate) / 12.0
            monthly_unpaid_balance = (bal) - (monthly_payment)
            updated_balance_each_month = (monthly_unpaid_balance) + \
            (monthly_interest_rate * monthly_unpaid_balance)
            bal = updated_balance_each_month
            month += 1
    return monthly_payment

def main():
    '''
    function call
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest payment: "+str(paying_debt_offina_year(data[0], data[1])))

if __name__ == "__main__":
    main()
