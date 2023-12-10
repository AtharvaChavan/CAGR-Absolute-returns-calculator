def calculate_cagr_from_absolute_return(absolute_return, n):
    absolute_return_decimal = absolute_return / 100
    fv = 1 + absolute_return_decimal
    return (fv)**(1/n) - 1

def calculate_absolute_return_from_cagr(cagr, n):
    cagr_decimal = cagr / 100
    fv = (1 + cagr_decimal) ** n
    absolute_return = (fv - 1) * 100
    return absolute_return

def main():
    while True:
        print("1. Calculate CAGR from absolute return")
        print("2. Calculate absolute return from CAGR")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            absolute_return = float(input("Enter absolute return in percentage: "))
            n = float(input("Enter number of years: "))
            cagr = calculate_cagr_from_absolute_return(absolute_return, n)
            print(f"CAGR: {cagr:.2%}")
        elif choice == '2':
            cagr = float(input("Enter CAGR in percentage: "))
            n = float(input("Enter number of years: "))
            absolute_return = calculate_absolute_return_from_cagr(cagr, n)
            print(f"Absolute Return: {absolute_return:.2f}%")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
