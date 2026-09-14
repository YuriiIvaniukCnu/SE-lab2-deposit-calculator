def main():
    amount = float(input("Enter deposit amount: "))
    interest_year = int(input("Enter interest rate (in %): "))
    term = int(input("Enter deposit term (in months): "))

    interest_month = (interest_year / 100) / 12
    for i in range(0, term):
        amount += amount * interest_month
        print(amount, " ", i, " ", interest_month)

    print("Balance:", amount)

if __name__ == "__main__":
    main()