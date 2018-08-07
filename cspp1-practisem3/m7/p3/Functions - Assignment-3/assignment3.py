

def payingDebtOffInAYear(balance, annualInterestRate):


def main():
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1]))
    
if __name__== "__main__":
    main()
