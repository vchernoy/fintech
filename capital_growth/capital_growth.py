def capital0(years=10, contribution=10000., price_growth=5., dividend_yield=2., taxed=0., fee=0.):
    capital = contribution * ((100. + price_growth - fee + dividend_yield) * 0.01) ** years
    after_tax_capital = capital - (capital - contribution) * taxed * 0.01
    return after_tax_capital, capital


def capital1(years=10, contribution=10000., price_growth=5., dividend_yield=2., taxed=0., fee=0.):
    base = contribution
    capital = contribution
    for _ in range(years):
        the_dividends = capital * dividend_yield * (100. - taxed) * 0.01 * 0.01
        the_growth = capital * (price_growth - fee) * 0.01
        base += the_dividends
        capital += the_growth + the_dividends

    return capital - (capital - base) * taxed * 0.01, capital, base


res = capital1(years=5)
print(res)

res = capital0(years=5)
print(res)

print(700 * 0.85)

years = (2, 5, 10, 15, 20)

print('Roth')
for y in years:
    res = capital1(years=y)
    print('{:2d}: {:5.0f}'.format(y, res[0]))

print('Roth, fee:1%')
for y in years:
    res = capital1(years=y, fee=1.)
    print('{:2d}: {:5.0f}'.format(y, res[0]))

print('Roth, fee:2%')
for y in years:
    res = capital1(years=y, fee=2.)
    print('{:2d}: {:5.0f}'.format(y, res[0]))

fed_tax = 15.
print('taxable')
for y in years:
    res = capital1(years=y, taxed=fed_tax)
    print('{:2d}: {:5.0f}'.format(y, res[0]), res[1])

print('taxable, 0')
for y in years:
    res = capital0(years=y, taxed=fed_tax)
    print('{:2d}: {:5.0f}'.format(y, res[0]))

state_tax = 9.3
print('taxable, state tax')
for y in years:
    res = capital1(years=y, taxed=fed_tax + state_tax)
    print('{:2d}: {:5.0f}'.format(y, res[0]), res[1])

print('taxable, state tax, 0')
for y in years:
    res = capital0(years=y, taxed=fed_tax + state_tax)
    print('{:2d}: {:5.0f}'.format(y, res[0]))

years = (2, 3, 4, 5, 7, 10, 15, 20, 25, 30)

for y in years:
    g1 = capital1(years=y, fee=1.)[0]
    g2 = capital0(years=y, taxed=fed_tax)[0]
    print('{:2d}: roth+1%fee={:5.0f}, taxable={:5.0f}, delta={:5.1f}'.format(y, g1, g2, 100. * (g2 - g1) / g2))

for y in years:
    g1 = capital1(years=y, fee=2.)[0]
    g2 = capital0(years=y, taxed=fed_tax)[0]
    print('{:2d}: roth+2%fee={:5.0f}, taxable={:5.0f}, delta={:5.1f}'.format(y, g1, g2, 100. * (g2 - g1) / g2))

for y in years:
    g1 = capital1(years=y, fee=1.)[0]
    g2 = capital0(years=y, taxed=fed_tax + state_tax)[0]
    print('{:2d}: roth+1%fee={:5.0f}, taxable+state={:5.0f}, delta={:5.1f}'.format(y, g1, g2, 100. * (g2 - g1) / g2))

for y in years:
    g1 = capital1(years=y, fee=2.)[0]
    g2 = capital0(years=y, taxed=fed_tax + state_tax)[0]
    print('{:2d}: roth+2%fee={:5.0f}, taxable+state={:5.0f}, delta={:5.1f}'.format(y, g1, g2, 100. * (g2 - g1) / g2))

for y in (0, 10, 20, 30):
    gRoth, gRoth0, gRoseBase = capital1(years=y, taxed=0)
    gTaxable, gTaxable0, gTaxableBase = capital1(years=y, taxed=15)
    print(
        '{:2d}: roth={:5.0f} ({:5.0f}), taxable={:5.0f} ({:5.0f}, taxed={:5.0f}, taxes={:5.0f}), delta={:5.1f}'.format(
            y, gRoth, gRoth0, gTaxable, gTaxable0, gTaxable0 - gTaxableBase, 0.15 * (gTaxable0 - gTaxableBase),
            100. * (gRoth - gTaxable) / gRoth))

