import math

def calculate_cagr(pv, fv, n):
    return (fv/pv)**(1/n) - 1

def calculate_absolute_percentage(pv, fv):
    return ((fv - pv) / pv) * 100

def calculate_time_period(pv, fv, cagr):
    return math.log(fv/pv) / math.log(1 + cagr)

# Example usage:
pv = 324200  # Initial value
fv = 387200  # Final value
n = 2      # Number of years

cagr = calculate_cagr(pv, fv, n)
absolute_percentage = calculate_absolute_percentage(pv, fv)
time_period = calculate_time_period(pv, fv, cagr)

print(f"CAGR: {cagr:.2%}")
print(f"Absolute Percentage Growth: {absolute_percentage:.2f}%")
print(f"Time Period: {time_period:.2f} years")
