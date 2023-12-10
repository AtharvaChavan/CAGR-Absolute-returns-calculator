def calculate_absolute_return_from_cagr(cagr, n):
    # Convert CAGR from percentage to decimal
    cagr_decimal = cagr / 100
    # Calculate the final value assuming the initial value is 1
    fv = (1 + cagr_decimal) ** n
    # Calculate absolute return
    absolute_return = (fv - 1) * 100
    return absolute_return

# Example usage:
cagr = 15  # CAGR in percentage
n = 2      # Number of years

absolute_return = calculate_absolute_return_from_cagr(cagr, n)

print(f"Entered CAGR Return: {cagr:}%")
print(f"Entered Years: {n:}%")
print(f"Absolute Return: {absolute_return:.2f}%")


input("Press Enter to exit...")  # This will pause the execution