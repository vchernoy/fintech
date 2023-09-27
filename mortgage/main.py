from dataclasses import dataclass
from math import ceil


@dataclass
class ExtraPayment:
    payment: float
    start_month: int
    end_month: int
    every_ith_month: int


@dataclass
class LoanDesc:
    amount: float
    rate: float
    term: float
    extras: list[ExtraPayment]
    inflation: float


@dataclass
class Repayment:
    principal: float
    interest: float
    balance: float
    net_value_payment: float


@dataclass
class LoanRepayment:
    monthly_payment: float
    monthly_schedule: tuple[Repayment, ...]
    annual_schedule: tuple[Repayment, ...]
    total: Repayment


def calculate_mortgage(loan: LoanDesc) -> LoanRepayment:
    monthly_rate = loan.rate / 100 / 12
    total_payments = ceil(loan.term * 12)
    monthly_payment = (loan.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
    monthly_schedule = []
    balance = loan.amount

    annual_schedule = []

    monthly_real_value_erosion = 1 / ((1 + loan.inflation / 100) ** (1 / 12))

    for month in range(total_payments):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        for extra in loan.extras:
            if extra.payment > 0 and extra.start_month <= month <= extra.end_month and (
                    month - extra.start_month) % extra.every_ith_month == 0:
                principal += extra.payment

        if principal >= balance:
            principal = balance
            balance = 0
        else:
            balance -= principal

        payment = principal + interest

        monthly_schedule.append(
            Repayment(
                principal=principal,
                interest=interest,
                balance=balance,
                net_value_payment=payment * monthly_real_value_erosion ** month),
        )

        if month % 12 == 11:
            annual_schedule.append(
                Repayment(
                    principal=sum(monthly.principal for monthly in monthly_schedule[-12:]),
                    interest=sum(monthly.interest for monthly in monthly_schedule[-12:]),
                    balance=balance,
                    net_value_payment=sum(monthly.net_value_payment for monthly in monthly_schedule[-12:]),
                )
            )

        if balance <= 0:
            break

    payments_done = len(monthly_schedule)
    if (payments_done - 1) % 12 != 11:
        annual_schedule.append(
            Repayment(
                principal=sum(monthly.principal for monthly in monthly_schedule[-(payments_done % 12):]),
                interest=sum(monthly.interest for monthly in monthly_schedule[-(payments_done % 12):]),
                balance=balance,
                net_value_payment=sum(
                    monthly.net_value_payment for monthly in monthly_schedule[-(payments_done % 12):]),
            )
        )

    return LoanRepayment(
        monthly_payment=monthly_payment,
        monthly_schedule=tuple(monthly_schedule),
        annual_schedule=tuple(annual_schedule),
        total=Repayment(
            principal=sum(annual.principal for annual in annual_schedule),
            interest=sum(annual.interest for annual in annual_schedule),
            balance=annual_schedule[-1].balance,
            net_value_payment=sum(annual.net_value_payment for annual in annual_schedule),
        ),
    )


def get_input() -> LoanDesc:
    default = LoanDesc(
        amount=500000,
        rate=8,
        term=30,
        extras=[],
        inflation=3.126478312,
    )

    loan_amount = float(input(f'Enter the loan amount (${default.amount:,.2f}): ') or f'{default.amount}')
    loan_rate = float(input(f'Enter the annual loan rate ({default.rate}%): ') or f'{default.rate}')
    loan_term = float(input(f'Enter the loan term (in years, {default.term}): ') or f'{default.term}')

    loan_term_months = ceil(loan_term * 12)
    default_extra = ExtraPayment(payment=0, start_month=0, end_month=loan_term_months, every_ith_month=1)
    extras: list[ExtraPayment] = []

    while True:
        extra_payment = float(
            input(f'Enter the extra payment (${default_extra.payment:,.2f}): ') or f'{default_extra.payment}')
        extra_payment = max(extra_payment, default_extra.payment)
        if extra_payment <= 0:
            break

        start_month = int(input(
            f'Enter the start month for extra payments ({default_extra.start_month}): ') or f'{default_extra.start_month}')
        start_month = max(start_month, default_extra.start_month)

        end_month = int(input(
            f'Enter the start month for extra payments ({default_extra.end_month}): ') or f'{default_extra.end_month}')
        end_month = min(end_month, default_extra.end_month)

        every_ith_month = int(input(
            f'Enter the frequency of extra payments (each, {default_extra.every_ith_month} month): ') or f'{default_extra.every_ith_month}')
        every_ith_month = max(every_ith_month, default_extra.every_ith_month)

        extras.append(
            ExtraPayment(
                payment=extra_payment,
                start_month=start_month,
                end_month=end_month,
                every_ith_month=every_ith_month,
            )
        )

    inflation = float(input(f'Enter the inflation rate ({default.inflation:,.2f}%): ') or f'{default.inflation}')
    return LoanDesc(
        amount=loan_amount,
        rate=loan_rate, term=loan_term,
        extras=extras,
        inflation=inflation,
    )


def display_output(repayment: LoanRepayment):
    print(f"The monthly mortgage payment: ${repayment.monthly_payment:,.2f}")
    total_payments = repayment.total.principal + repayment.total.interest
    num_payments = len(repayment.monthly_schedule)
    print(f"The average monthly mortgage payment: ${total_payments / num_payments:,.2f}")
    print(f"The number of payments: {num_payments}")

    print(f"The total interest paid: ${repayment.total.interest:,.2f}")
    print(f"The total of payments: ${total_payments:,.2f}")
    print(f"The net value of payments: ${repayment.total.net_value_payment:,.2f}")

    for year, annual in enumerate(repayment.annual_schedule, start=1):
        print(
            f"Year {year}: principal=${annual.principal:,.2f}, interest=${annual.interest:,.2f}, payment=${annual.principal + annual.interest:,.2f}, net value of payments=${annual.net_value_payment:,.2f}, balance=${annual.balance:,.2f}")

    print()

    for month, monthly in enumerate(repayment.monthly_schedule, start=1):
        print(
            f"Month {month}: principal=${monthly.principal:,.2f}, interest=${monthly.interest:,.2f}, payment=${monthly.principal + monthly.interest:,.2f}, net value of payment=${monthly.net_value_payment:,.2f}, balance=${monthly.balance:,.2f}")


def main():
    mortgage_data = get_input()
    repayment = calculate_mortgage(mortgage_data)
    display_output(repayment)


main()
