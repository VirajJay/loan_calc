def calculate_loan_term(principal, annual_rate, offset, monthly_payment):
    """
    Calculate how many months it takes to repay a home loan with a given monthly payment and offset.
    
    :param principal: Initial loan amount (float)
    :param annual_rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
    :param offset: Offset account amount (float)
    :param monthly_payment: Fixed monthly payment amount (float)
    :return: Number of months to repay the loan, total interest paid
    """
    monthly_rate = annual_rate / 12
    balance = principal
    months = 0
    total_interest = 0.0

    while balance > 0:
        effective_balance = max(0, balance - offset)
        interest = effective_balance * monthly_rate
        total_interest += interest
        balance += interest - monthly_payment
        months += 1

        # Avoid infinite loop if payment is too low
        if months > 1000*12:  # arbitrarily cap at 1000 years
            raise ValueError("Loan will never be repaid at this payment amount.")

    return months, total_interest

loan_amount = 640000
offset = 50000
annual_interest_rate = 0.0593
monthly_payment = 5000 # Your chosen monthly payment

print("Interest_rate: {}%".format(annual_interest_rate*100))
print("Monthly payment: {}".format(monthly_payment))
print("offset (with parent help): {}".format(offset))

months, interest_paid = calculate_loan_term(
    loan_amount, annual_interest_rate, offset, monthly_payment
)

years = months // 12
extra_months = months % 12

print(f"Loan repaid in {years} years and {extra_months} months.")
print(f"Total interest paid: ${interest_paid:.2f}")
