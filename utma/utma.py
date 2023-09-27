def calc(value0, interval, tax_harvest=True, grow_ratio=5., dividend_yield=2., tax=0., tax_exempt=0., ):
    v0 = value0
    total_dividends = 0.
    base_value = v0
    for i in range(interval):
        price_growth = v0 * grow_ratio * 0.01
        dividends = v0 * dividend_yield * 0.01
        taxed_dividends = max(dividends - tax_exempt, 0)
        dividends -= taxed_dividends * tax * 0.01

        tax_exempt_left = max(tax_exempt - dividends, 0)
        price_growth_harvested = min(price_growth, tax_exempt_left)

        capital_growth = price_growth + dividends
        value = v0 + capital_growth

        base_value = base_value + dividends + price_growth_harvested * (1 if tax_harvest else 0)
        total_dividends += dividends
        # print('{:2} {:6.0f} => {:6.0f} [{:6.0f}], {:5.0f} ={:5.0f} +{:5.0f} {:6.0f}'.format(i+1, v0, v1, base_value, capital_growth, price_growth, dividends, price_growth_harvested))
        v0 = value

    taxable = max(value - base_value - tax_exempt, 0)
    return value, base_value, total_dividends, taxable


K = 1000.

tax = 15.
tax_exempt = 2 * 1050.

tax_backet = 39375.

value0 = 30. * K
interval = 20

grow_ratio = 5.
dividend_yield = 2.

value, base_value, total_dividends, _ = calc(value0, interval, tax_harvest=True, grow_ratio=grow_ratio,
                                             dividend_yield=dividend_yield, tax=0., tax_exempt=0.)
taxable = 0.
after_tax_value = value
print(
    '529 plan, Qualified use:      {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

taxable = value - value0
after_tax_value = value - taxable * (12 + 10) * 0.01
print(
    '529 plan, Non-qualified use:  {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

value, base_value, total_dividends, _ = calc(value0, interval, tax_harvest=True, grow_ratio=grow_ratio,
                                             dividend_yield=dividend_yield, tax=tax, tax_exempt=tax_exempt)
taxable = max(value - base_value - tax_exempt * 0.5 - tax_backet, 0)
after_tax_value = value - taxable * tax * 0.01
print(
    'UTMA plan, Tax-harvesting:    {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

value, base_value, total_dividends, _ = calc(value0, interval, tax_harvest=False, grow_ratio=grow_ratio,
                                             dividend_yield=dividend_yield, tax=tax, tax_exempt=tax_exempt)
taxable = max(value - base_value - tax_exempt * 0.5 - tax_backet, 0)
after_tax_value = value - taxable * tax * 0.01
print(
    'UTMA plan, No tax-harvesting: {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

value, base_value, total_dividends, taxable = calc(value0, interval, tax_harvest=True, grow_ratio=grow_ratio,
                                                   dividend_yield=dividend_yield, tax=tax, tax_exempt=0.)
taxable = max(taxable - tax_backet, 0)
after_tax_value = value - taxable * tax * 0.01
print(
    'Taxable account:              {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

value, base_value, total_dividends, taxable = calc(value0, interval, tax_harvest=True, grow_ratio=7., dividend_yield=0.,
                                                   tax=tax, tax_exempt=0.)
taxable = max(taxable - tax_backet, 0)
after_tax_value = value - taxable * tax * 0.01
print(
    'Taxable account 7%:           {:6.0f} ={:5.0f} +{:5.0f}, harvested={:6.0f}, total_dividends={:5.0f}, after_tax_value={:6.0f}, taxable={:5.0f}'.format(
        value, base_value, value - base_value, base_value - value0 - total_dividends, total_dividends, after_tax_value,
        taxable))

