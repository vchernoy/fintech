def calculate_investment(years: int, annual_growth: float, annual_charges: list[float], initial: float, annual_contribution: float, management_fee: float=0, inflation: float=3.126478312) -> float:
    annual_real_value_erosion = 1 / (1+inflation/100)
    monthly_real_value_erosion = annual_real_value_erosion**(1/12)

    annual_growth_rate = (1 + annual_growth/100)
    monthly_growth_rate = annual_growth_rate**(1/12)

    expense_ratio = management_fee/100
    monthly_expense_ratio = 1 - (1-expense_ratio)**(1/12)

    total = initial

    total_fees = 0
    real_value_fees = 0

    total_contributions = total
    real_value_contributions = total

    net_total = total

    for year in range(years):
        monthly_contributions = annual_contribution/12
        monthly_charges = annual_charges[year]/12

        for month in range(12):
            real_value_erosion = monthly_real_value_erosion ** (year * 12 + month)

            total_contributions += monthly_contributions
            real_value_contributions += monthly_contributions * real_value_erosion

            total += monthly_contributions

            monthly_fees = monthly_charges + total * monthly_expense_ratio
            total_fees += monthly_fees
            real_value_fees += monthly_fees * real_value_erosion

            total *= monthly_growth_rate
            total -= monthly_fees

            net_total += monthly_contributions
            net_total *= monthly_growth_rate

    real_value = total * annual_real_value_erosion**years
    real_net = net_total * annual_real_value_erosion**years

    losses = (net_total - total) / net_total * 100
    print(f'net_total=${net_total:,.0f}, total=${total:,.0f}, real_value=${real_value:,.0f}, total_fees=${total_fees:,.0f}, real_value_fees=${real_value_fees:,.0f}, total_contributions=${total_contributions:,.0f}, real_value_contributions=${real_value_contributions:,.0f}, management_fee={management_fee:.2f}%, losses={losses:,.2f}%')
    return total


def main():
    total_iul = calculate_investment(20, 7, [3502]*9 + [2702]*5 + [2705, 1511, 1590, 1674, 1762, 1852], 0, 20000)
    total_nofees = calculate_investment(20, 7, [0]*20, 0, 20000)
    capital_lost = (total_nofees - total_iul) / total_nofees * 100
    print(f'{capital_lost=:,.2f}%')

    total_50fee = calculate_investment(20, 6.5, [0]*20, 0, 20000)
    total_100fee = calculate_investment(20, 6, [0]*20, 0, 20000)
    total_150fee = calculate_investment(20, 5.5, [0]*20, 0, 20000)
    total_200fee = calculate_investment(20, 5, [0]*20, 0, 20000)

    total_50fee = calculate_investment(20, 7, [0]*20, 0, 20000, 0.5)
    total_100fee = calculate_investment(20, 7, [0]*20, 0, 20000, 1)
    total_130fee = calculate_investment(20, 7, [0]*20, 0, 20000, 1.3)

    print()

    total_iul30y = calculate_investment(30, 7, [3502]*9 + [2702]*5 + [2705, 1511, 1590, 1674, 1762, 1852] + [1852]*10, 0, 12000)
    total_capital = calculate_investment(30, 7, [0]*30, 0, 12000)


