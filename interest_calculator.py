def home_loan_interest(principal, annual_rate, years, offset):
    """
    Calculate the total interest paid on a home loan with an offset account.
    
    :param principal: Initial loan amount (float)
    :param annual_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    :param years: Loan term in years
    :param offset: Offset amount that reduces interest calculation
    :return: Total interest paid over the loan period
    """
    monthly_rate = annual_rate / 12
    months = years * 12
    effective_principal = principal - offset

    monthly_payment = (effective_principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    total_interest = (monthly_payment * months) - effective_principal

    return total_interest, monthly_payment

# Example usage
loan_amount = 500000
offset = 150000
annual_interest_rate = 0.0583
loan_term_years = 30

total_interest_paid, monthly_payment = home_loan_interest(
    loan_amount, annual_interest_rate, loan_term_years, offset
)

print(f"Total interest paid over {loan_term_years} years: ${total_interest_paid:.2f}")
print(f"Monthly payment: ${monthly_payment:.2f}")
