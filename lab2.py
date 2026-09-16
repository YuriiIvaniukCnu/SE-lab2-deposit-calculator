from decimal import Decimal, InvalidOperation

def calculate_deposit(amount, interest_year, term):
    print(" ")

    interest_month = (interest_year / 100) / 12
    for i in range(0, term):
        amount += amount * interest_month
        print(f"Month: {i+1} | {amount:.2f}")

    print(f"\nTotal: {amount:.2f}")

def read_number(prompt, cast=Decimal, default=None):
    while True:
        raw = input(prompt)

        if not raw and default is not None:
            return default

        try:
            value = cast(raw)
        except (ValueError, InvalidOperation):
            if cast == int:
                print("Please enter a whole number")
                continue
            print("Please enter a number")
            continue

        if value > 0:
            return value
        else:
            print("Enter only numbers above 0")
            continue

def main():
    amount = read_number("Enter the amount to be deposited: ")
    interest_year = read_number("Enter interest rate (% annual): ")
    term = read_number("Enter deposit term (months, default 24): ", int, default=24)

    calculate_deposit(amount, interest_year, term)

if __name__ == "__main__":
    main()