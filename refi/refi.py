class Res:
    def __init__(self, rate, loan, years, annual_payments=12, year=2021, tax=22.):
        self.total_payments = years * annual_payments
        self.monthly_principal = [0.] * self.total_payments
        self.monthly_interest = [0.] * self.total_payments
        self.monthly_balance = [0.] * self.total_payments
        self.monthly_payment = [0.] * self.total_payments
        self.monthly_tax_deductions = [0.] * self.total_payments
        self.monthly_aftertax_payment = [0.] * self.total_payments

        self.annual_principal = [0.] * years
        self.annual_interest = [0.] * years
        self.annual_balance = [0.] * years
        self.annual_payment = [0.] * years
        self.annual_tax_deductions = [0.] * years
        self.annual_aftertax_payment = [0.] * years

        self.total_principal = 0.
        self.total_interest = 0.
        self.total_payment = 0.

        self.annual_rate = rate
        self.monthly_rate = rate / annual_payments

        self.loan = loan
        self.years = years

        self.year = year

        self.total_tax_deductions = 0.
        self.total_aftertax_payment = 0.
        self.tax = tax


def finance(rate, loan, years, tax=22., annual_payments=12, year=2021):
    res = Res(rate, loan, years, annual_payments, year, tax)

    # r = (1. + rate * 0.01)**(1./payments) - 1.
    r = res.monthly_rate * 0.01
    p = 1. / (1. + r)

    N = res.total_payments
    A = r * loan / (1. - p ** N)

    # In = A * ( 1. - p**(N-n) )
    # Ln = In / r
    # Pn = A - In

    # P = res.monthly_principal
    # I = res.monthly_interest
    # L = res.monthly_balance
    for n in range(N):
        Pn = A * p ** (N - n)
        In = A - Pn
        Ln = In / r
        res.monthly_principal[n] = Pn
        res.monthly_interest[n] = In
        res.monthly_balance[n] = Ln
        res.monthly_payment[n] = Pn + In
        res.monthly_tax_deductions[n] = res.monthly_interest[n] * res.tax * 0.01
        res.monthly_aftertax_payment[n] = res.monthly_payment[n] - res.monthly_tax_deductions[n]

    for n in range(N + 1):
        if n > 0 and n % annual_payments == 0:
            m = n // annual_payments - 1
            res.annual_principal[m] = sum(res.monthly_principal[n - annual_payments:n])
            res.annual_interest[m] = sum(res.monthly_interest[n - annual_payments:n])
            res.annual_payment[m] = sum(res.monthly_payment[n - annual_payments:n])
            res.annual_balance[m] = res.monthly_balance[n] if n < N else 0.
            res.annual_tax_deductions[m] = res.annual_interest[m] * res.tax * 0.01
            res.annual_aftertax_payment[m] = res.annual_payment[m] - res.annual_tax_deductions[m]

    res.total_principal = sum(res.annual_principal)
    res.total_interest = sum(res.annual_interest)
    res.total_payment = sum(res.annual_payment)
    res.total_tax_deductions = res.total_interest * res.tax * 0.01
    res.total_aftertax_payment = res.total_payment - res.total_tax_deductions
    # res.tax = tax
    # res.year = year

    return res


def pr_res(res, print_table=True):
    print('loan:{:10.2f}, annual_rate:{:6.3f}%, monthly_rate:{:6.3f}%, years:{:4}'.format(res.loan, res.annual_rate,
                                                                                          res.monthly_rate, res.years))

    print('year   interest  principal    balance    payment   after-tax')

    for m in range(len(res.annual_balance)):
        y = m + res.year
        if print_table:
            print('{:2} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}'.format(
                y, res.annual_interest[m], res.annual_principal[m], res.annual_balance[m], res.annual_payment[m],
                res.annual_aftertax_payment[m]))

    print('total{:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}'.format(
        res.total_interest, res.total_principal, 0., res.total_payment, res.total_aftertax_payment))

    print()
    # P(n+1) = P(n) / p
    # L(n+1) - L(n) = r * L(n) - A
    # I(n+1) = A - P(n)
    # I(n) = A - P(n-1)
    # I(n+1) - I(n) = P(n-1) - P(n)

    # P(n) = A - I(n+1)
    # P(n-1) = A - I(n)
    # p * (A - I(n+1)) = A - I(n)
    # A - I(n+1) = (A - I(n)) / p
    # I(n+1) = A - (A - I(n)) / p = A * (1 - 1/p) + I(n) / p = I(n) / p - r * A
    # I(n+1) = I(n) / p - r * A


def analyse_refi(res, refi_res, print_table=True):
    aftertax_paid = 0.
    refi_aftertax_paid = 0.

    print('fina: loan: {:10.2f}, annual_rate: {:5.3f}, years: {:4}, monthly_payment: {:6.2f}'.format(res.loan,
                                                                                                     res.annual_rate,
                                                                                                     res.years,
                                                                                                     res.monthly_payment[
                                                                                                         0]))

    print('refi: loan: {:10.2f}, annual_rate: {:5.3f}, years: {:4}, monthly_payment: {:6.2f}'.format(refi_res.loan,
                                                                                                     refi_res.annual_rate,
                                                                                                     refi_res.years,
                                                                                                     refi_res.monthly_payment[
                                                                                                         0]))

    if print_table:
        print('year   after-tax saving')

    for m in range(max(len(res.annual_balance), len(refi_res.annual_balance))):
        y = m + res.year
        annual_aftertax_payment = res.annual_aftertax_payment[m] if m < len(res.annual_balance) else 0
        refi_annual_aftertax_payment = refi_res.annual_aftertax_payment[m] if m < len(refi_res.annual_balance) else 0

        if print_table:
            print('{:2} {:10.2f}'.format(y, annual_aftertax_payment - refi_annual_aftertax_payment))

    print('total after-tax saving: {:10.2f}'.format(res.total_aftertax_payment - refi_res.total_aftertax_payment))

    for m in range(max(len(res.annual_balance), len(refi_res.annual_balance))):
        y = m + res.year

        annual_aftertax_payment = res.annual_aftertax_payment[m] if m < len(res.annual_balance) else 0
        annual_balance = res.annual_balance[m] if m < len(res.annual_balance) else 0
        aftertax_paid += annual_aftertax_payment
        total_cost = aftertax_paid + annual_balance

        refi_annual_aftertax_payment = refi_res.annual_aftertax_payment[m] if m < len(refi_res.annual_balance) else 0
        refi_annual_balance = refi_res.annual_balance[m] if m < len(refi_res.annual_balance) else 0
        refi_aftertax_paid += refi_annual_aftertax_payment
        refi_total_cost = refi_aftertax_paid + refi_annual_balance

        if refi_total_cost < total_cost:
            print('after {} years, we have break even at {} year'.format(m, y))
            print('aftertax_paid-refi_aftertax_paid: {}'.format(aftertax_paid - refi_aftertax_paid))
            print('annual_balance-refi_annual_balance: {}'.format(annual_balance - refi_annual_balance))
            break
    print()


if 0:
    res = finance(4.125, 220000., 25)
    pr_res(res)

    ref_res = finance(2.875, 220000. + 14000, 25)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

if 0:
    res = finance(4.75, 140416., 28, tax=0.)
    pr_res(res)

    ref_res = finance(3.75, 140416 + 16000, 30, tax=0.)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

if 0:
    loan = 189000
    tax = 0.

    res = finance(4.90, loan, 28, tax=tax)
    pr_res(res, False)

    for refi_rate, refi_price in [(2.250, 11151.36), (2.750, 4181.36), (2.875, 2864.64), (3., 1960.32),
                                  (3.125, 1560.96), (3.250, 679), (3.375, -172.80), (3.5, -825.6), (3.625, -1228.8)]:
        ref_res = finance(refi_rate, loan + 3000 + refi_price, 30, tax=tax)
        # pr_res(ref_res, False)
        analyse_refi(res, ref_res, False)

if 0:
    loan = 100000
    years = 30
    tax = 22.
    res = finance(4., loan, years, tax=tax)
    pr_res(res)

    ref_res = finance(3., loan + 13237.83 * 0.5, years, tax=tax)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

if 0:
    loan = 100000
    years = 30
    tax = 0.
    res = finance(4., loan, years, tax=tax)
    pr_res(res)

    ref_res = finance(3.5, loan, years, tax=tax)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

if 0:
    loan = 180000
    years = 15
    tax = 0.
    res = finance(3.25, loan, years - 3, tax=tax)
    pr_res(res)

    ref_res = finance(2.25, loan + 12000, years, tax=tax)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

K = 1000
M = K * K
if 0:
    loan = 100 * K
    years = 20
    tax = 0.
    res = finance(3.5, loan, years, tax=tax)
    pr_res(res)

    ref_res = finance(3., loan + 3 * K, years, tax=tax)
    pr_res(ref_res)
    analyse_refi(res, ref_res)

if 1:
    loan = 364.251 * K
    years = 30
    tax = 0.
    res = finance(4., loan + 368, years, tax=tax)
    pr_res(res)

    ref_res = finance(2.875, loan + 6072, years, tax=tax)
    pr_res(ref_res)
    analyse_refi(res, ref_res)
