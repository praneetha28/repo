"'#input'"
def paying_debt_offina_year(balance, annual_interest_rate):
    '''
    function
    '''
    monthly_interest_rate = (annual_interest_rate) / 12.0
    monthly_payment_lower_bound = balance / 12
    monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    new_balance = balance
    increment = 0.0001
    guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2
    while True:
        month = 1
        while month <= 12:
            new_balance = new_balance - guess
            new_balance = new_balance + (monthly_interest_rate * new_balance)
            month += 1
        if new_balance > 0 and new_balance > increment:
            monthly_payment_lower_bound = guess
            new_balance = balance
        elif new_balance < 0 and new_balance < -increment:
            monthly_payment_upper_bound = guess
            new_balance = balance
        else:
            return guess

        guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2


def main():
    '''
    call
    '''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+str(round(paying_debt_offina_year(data[0], data[1]), 2)))

if __name__ == "__main__":
    main()
