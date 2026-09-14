def calculate_deposit(amount, interest_year, term):
    print(" ")

    interest_month = (interest_year / 100) / 12
    for i in range(0, term):
        amount += amount * interest_month
        print("Month: ",i+1, " | ", amount)

    print("\nTotal:", amount)
def main():
    amount = float(input("Enter deposit amount: "))
    interest_year = int(input("Enter interest rate (% annual): "))
    term = int(input("Enter deposit term (months): "))

    calculate_deposit(amount, interest_year, term)

if __name__ == "__main__":
    main()