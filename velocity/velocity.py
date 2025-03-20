from scipy.optimize import fsolve


def daily_payment(annual_interest_rate, P, days):
    daily_interest_rate = annual_interest_rate / 365  # Convert to daily rate

    # Function to find the daily payment required to fully pay off in 30 days
    def balance_after_30_days(D):
        remaining_balance = P  # Start with the initial balance
        for _ in range(days):
            daily_interest = remaining_balance * daily_interest_rate  # Accrue interest
            remaining_balance += daily_interest  # Add interest to balance
            remaining_balance -= D  # Make daily payment
        return remaining_balance  # We want this to be zero

    # Solve for D (daily payment required)
    D_solution = fsolve(balance_after_30_days, P / days)[0]
    return D_solution


def compute(annual_interest_rate, P, days, D):
    daily_rate = annual_interest_rate / 365  # Daily interest rate

    remaining_balance = P
    total_interest = 0

    for day in range(days):
        daily_interest = remaining_balance * daily_rate  # Interest accrues first
        total_interest += daily_interest  # Track total interest paid
        remaining_balance += daily_interest  # Add interest to balance
        remaining_balance -= D  # Then make the daily payment

    return total_interest, remaining_balance


def pay_interest_only(annual_interest_rate, P, days, monthly_payments):
    daily_rate = annual_interest_rate / 365  # Daily interest rate

    remaining_balance = P
    total_interest = 0

    for day in range(1, days + 1):
        daily_interest = remaining_balance * daily_rate  # Interest accrues first
        total_interest += daily_interest  # Track total interest paid
        remaining_balance += daily_interest  # Add interest to balance

        if day % 30 == 0:
            monthly_payments.append(total_interest)
            remaining_balance = P
            total_interest = 0

    if total_interest > 0:
        monthly_payments.append(total_interest)
        remaining_balance = P
        total_interest = 0


def hysa(hysa_annual_rate, days, D):
    hysa_daily_rate = hysa_annual_rate / 365  # Convert to daily rate

    # Simulate the balance growth in HYSA over 30 days with daily contributions
    hysa_balance = 0
    total_hysa_interest = 0

    for _ in range(days):
        hysa_balance += D  # Add daily deposit
        daily_interest = hysa_balance * hysa_daily_rate  # Compute daily interest
        total_hysa_interest += daily_interest  # Track total interest
        hysa_balance += daily_interest  # Add interest to balance

    # Output the total balance accumulated in HYSA
    return hysa_balance, total_hysa_interest


def mortgage(mortgage_balance, mortgage_rate, monthly_payment, months_to_pay=None):
    mortgage_monthly_rate = mortgage_rate / 12  # Convert annual to monthly rate
    remaining_balance = mortgage_balance
    total_interest = 0

    month = 0
    while True:
        if months_to_pay is not None and month >= months_to_pay:
            break

        monthly_interest = remaining_balance * mortgage_monthly_rate
        total_interest += monthly_interest
        principal_paid = monthly_payment - monthly_interest
        remaining_balance -= principal_paid
        month += 1
        if remaining_balance <= 0:
            break

    return total_interest, month, remaining_balance


def normal_mortage(mortgage_balance, mortgage_rate, monthly_payment):
    print(
        f"Normal mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}"
    )
    total_interest, total_months, remaining_balance = mortgage(
        mortgage_balance, mortgage_rate, monthly_payment
    )
    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    print()


def hysa_mortgage(
    mortgage_balance,
    mortgage_rate,
    monthly_payment,
    hysa_balance,
    months_to_accumulate=1,
):
    print(
        f"HYSA + mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}, {hysa_balance=}"
    )
    total_interest, total_months, remaining_balance = mortgage(
        mortgage_balance, mortgage_rate, monthly_payment, months_to_accumulate
    )
    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    remaining_balance -= hysa_balance
    print(
        f"mortgage payments for {remaining_balance=}, {mortgage_rate=}, {monthly_payment=}"
    )
    interest, months, remaining_balance = mortgage(
        remaining_balance, mortgage_rate, monthly_payment
    )
    total_interest += interest
    total_months += months
    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    print()


def heloc_mortgage(mortgage_balance, mortgage_rate, monthly_payment, P):
    print(
        f"HELOC + mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}, {P=}"
    )
    total_interest, total_months, remaining_balance = mortgage(
        mortgage_balance - P, mortgage_rate, monthly_payment
    )
    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    print()


def repeat_hysa_mortgage(
    mortgage_balance,
    mortgage_rate,
    monthly_payment,
    hysa_balance,
    months_to_accumulate=1,
):
    print(
        f"repeat: HYSA + mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}, {hysa_balance=}"
    )
    total_months = 0
    total_interest = 0
    remaining_balance = mortgage_balance

    while True:
        month_interest, months, remaining_balance = mortgage(
            remaining_balance, mortgage_rate, monthly_payment, months_to_accumulate
        )
        total_months += months
        total_interest += month_interest
        remaining_balance -= hysa_balance
        if remaining_balance <= 0:
            break

    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    print()


def repeat_heloc_mortgage(mortgage_balance, mortgage_rate, monthly_payment, P):
    print(
        f"repeat: HELOC + mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}, {P=}"
    )
    total_months = 0
    total_interest = 0
    remaining_balance = mortgage_balance

    while True:
        remaining_balance -= P
        if remaining_balance <= 0:
            break
        month_interest, month, remaining_balance = mortgage(
            remaining_balance, mortgage_rate, monthly_payment, 1
        )
        total_months += month
        total_interest += month_interest

    print(f"{total_interest=}, {total_months=}, {remaining_balance=}")
    print()


def velocity(mortgage_balance, mortgage_rate, monthly_payment, P, heloc_interest_rate):
    print(
        f"Velocity mortgage payments for {mortgage_balance=}, {mortgage_rate=}, {monthly_payment=}, {P=}"
    )
    total_interest, total_months, remaining_balance = mortgage(
        mortgage_balance - P, mortgage_rate, monthly_payment
    )

    days = total_months * 30
    heloc_monthly_payments = []
    pay_interest_only(heloc_interest_rate, P, days, heloc_monthly_payments)

    A = sum(heloc_monthly_payments) / len(heloc_monthly_payments)
    print(
        f"{total_months=}, {total_interest=}, {len(heloc_monthly_payments)=}, {min(heloc_monthly_payments)}, {max(heloc_monthly_payments)}, {A=}"
    )
    # D = P / 30
    # compute(annual_interest_rate, P, days, D)

    total_interest, total_months, remaining_balance = mortgage(
        mortgage_balance, mortgage_rate, monthly_payment + A
    )
    print(f"{total_months=}, {total_interest=}, {A=}")


# HELOC
heloc_interest_rate = 0.08

month_days = 30  # Number of days in the month

months_to_accumulate = 1
P = 20000  # Allowed debt balance in HELOC
days = month_days * months_to_accumulate  # Number of days in the month

D = daily_payment(heloc_interest_rate, P, days)
heloc_interest, remaining_balance = compute(heloc_interest_rate, P, days, D)
M = D * days

print(f"{heloc_interest=}, {remaining_balance=}")
print(f"{P/days=}, {D=}, {P=}, {M=}")

# HYSA
hysa_annual_rate = 0.04  # 4% APY

hysa_balance, total_hysa_interest = hysa(hysa_annual_rate, days, D)
print(f"{hysa_balance=}, {total_hysa_interest=}")
print()

# Mortgage

mortgage_balance = 300_000
mortgage_rate = 0.07  # 7% APY
monthly_payment = 2000

normal_mortage(mortgage_balance, mortgage_rate, monthly_payment)
hysa_mortgage(mortgage_balance, mortgage_rate, monthly_payment, hysa_balance)
heloc_mortgage(mortgage_balance, mortgage_rate, monthly_payment, P)
repeat_hysa_mortgage(mortgage_balance, mortgage_rate, monthly_payment, hysa_balance)
repeat_heloc_mortgage(mortgage_balance, mortgage_rate, monthly_payment, P)


velocity(mortgage_balance, mortgage_rate, monthly_payment, P * 10, heloc_interest_rate)
