def calculate_cagr_from_absolute_return(absolute_return, n):
    # Convert absolute return percentage to a decimal
    absolute_return_decimal = absolute_return / 100
    # Calculate the final value assuming the initial value is 1
    fv = 1 + absolute_return_decimal
    # Calculate CAGR
    return (fv)**(1/n) - 1

# Example usage:
absolute_return = 100  # Absolute return in percentage
n = 4                # Number of years

cagr = calculate_cagr_from_absolute_return(absolute_return, n)


print(f"Entered absolute Return: {cagr:.2f}%")
print(f"Entered Years: {n:}%")
print(f"CAGR: {cagr:.2%}")

input("Press Enter to exit...")  # This will pause the execution