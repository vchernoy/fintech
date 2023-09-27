
def money(value: float, width: int = 6, currency: str = '$', sep: str = ',', precision: int = 0) -> str:
    s = f'{currency}{abs(value):{sep}.{precision}f}'
    if value < 0:
        s = '-' + s
    if len(s) < width:
        s = ' ' * (width - len(s)) + s
    return s


year = 1871


# dividends = [2]*len(dividends)

def read_hist(filepath):
    with open(filepath) as f:
        return tuple(reversed(tuple(float(p.replace(',', '')) for p in f.read().split())))


# prices = read_hist('sp500_prices_only.txt')
# dividends = read_hist('dividends_yield.txt')

old_prices = (
    4.44, 4.86, 5.11, 4.66, 4.54, 4.46, 3.55, 3.25, 3.58, 5.11, 6.19, 5.92, 5.81, 5.18, 4.24, 5.2, 5.58, 5.31, 5.24,
    5.38, 4.84, 5.51, 5.61, 4.32, 4.25, 4.27, 4.22, 4.88, 6.08, 6.1, 7.07, 8.12, 8.46, 6.68, 8.43, 9.87, 9.56, 6.85,
    9.06, 10.08, 9.27, 9.12, 9.3, 8.37, 7.48, 9.33, 9.57, 7.21, 7.85, 8.83, 7.11, 7.3, 8.9, 8.83, 10.58, 12.65, 13.4,
    17.53, 24.86, 21.71, 15.98, 8.3, 7.09, 10.54, 9.26, 13.76, 17.59, 11.31, 12.5, 12.3, 10.55, 8.93, 10.09, 11.85,
    13.49, 18.02, 15.21, 14.83, 15.36, 16.88, 21.21, 24.19, 26.18, 25.46, 35.6, 44.15, 45.43, 41.12, 55.62, 58.03,
    59.72, 69.07, 65.06, 76.45, 86.12, 93.32, 84.45, 95.04, 102.0, 90.31, 93.49, 103.3, 118.4, 96.11, 72.56, 96.86,
    103.8, 90.25, 99.71, 110.9, 133.0, 117.3, 144.3, 166.4, 171.6, 208.2, 264.5, 250.5, 285.4, 339.97, 325.49, 416.08,
    435.23, 472.99, 465.25, 614.42, 766.22, 963.36, 1248.77, 1425.59, 1335.63, 1140.21, 895.84, 1132.52, 1181.41,
    1278.73, 1424.16, 1378.76, 865.58, 1123.58, 1282.62, 1300.58, 1480.4, 1822.36, 2028.18, 1918.6, 2275.12, 2789.8,
    2607.39, 3044.02,
)

old_dividends = (
    5.49, 5.92, 7.47, 7.27, 6.86, 8.38, 5.85, 5.22, 4.07, 4.45, 5.32, 5.48, 6.18, 7.14, 4.62, 3.9, 4.74, 4.47, 4.14,
    4.78, 4.07, 4.36, 5.67, 4.88, 4.4, 4.27, 3.79, 3.54, 3.49, 4.37, 4.03, 4.1, 5.33, 3.76, 3.46, 4.07, 6.7, 4.43, 4.27,
    5.19, 5.16, 5.12, 5.97, 5.71, 4.54, 5.71, 10.15, 7.22, 5.94, 7.49, 6.29, 5.81, 6.2, 5.41, 4.82, 5.11, 4.41, 3.67,
    4.53, 6.32, 9.72, 7.33, 4.41, 4.86, 3.6, 4.22, 7.26, 4.02, 5.01, 6.36, 8.11, 6.2, 5.31, 4.89, 3.81, 4.69, 5.59,
    6.12, 6.89, 7.44, 6.02, 5.41, 5.84, 4.4, 3.61, 3.75, 4.44, 3.27, 3.1, 3.43, 2.82, 3.4, 3.07, 2.98, 2.97, 3.53, 3.06,
    2.88, 3.47, 3.49, 3.1, 2.68, 3.57, 5.37, 4.15, 3.87, 4.98, 5.28, 5.24, 4.61, 5.36, 4.93, 4.31, 4.58, 3.81, 3.33,
    3.66, 3.53, 3.17, 3.68, 3.14, 2.84, 2.7, 2.89, 2.24, 2.0, 1.61, 1.36, 1.17, 1.22, 1.37, 1.79, 1.61, 1.62, 1.76,
    1.76, 1.87, 3.23, 2.02, 1.83, 2.13, 2.2, 1.94, 1.92, 2.11, 2.03, 1.84, 2.09, 1.88,
)

'''
https://data.nasdaq.com/data/MULTPL/SP500_REAL_PRICE_MONTH-sp-500-real-price-by-month
https://data.nasdaq.com/api/v3/datasets/MULTPL/SP500_REAL_PRICE_MONTH.csv?api_key=wFdVJsiyX9NiR4uCYNg8&collapse=annual

https://data.nasdaq.com/data/MULTPL/SP500_DIV_YIELD_YEAR-sp-500-dividend-yield-by-year
https://data.nasdaq.com/api/v3/datasets/MULTPL/SP500_DIV_YIELD_YEAR.csv?api_key=wFdVJsiyX9NiR4uCYNg8&collapse=annual
'''

prices = (
    4.44, 4.74, 5.07, 4.42, 4.54, 4.37, 3.58, 3.25, 3.45, 4.92, 5.84, 6.01, 5.84, 5.34, 4.34, 5.2, 5.64, 5.27, 5.14,
    5.32, 4.6, 5.41, 5.51, 4.41, 4.3, 4.32, 4.22, 4.75, 5.65, 6.02, 6.87, 7.95, 8.05, 6.57, 8.25, 9.54, 9.84, 6.57,
    9.03, 10.3, 9.05, 9.11, 9.38, 8.04, 7.35, 9.48, 9.8, 6.8, 7.9, 8.92, 6.81, 7.31, 8.78, 8.55, 10.16, 12.46, 13.49,
    17.46, 23.15, 21.4, 15.51, 8.44, 6.82, 9.97, 9.26, 13.04, 17.06, 11.02, 12.69, 12.37, 10.53, 8.76, 9.52, 11.48,
    13.1, 17.33, 15.13, 15.03, 15.19, 16.54, 19.75, 23.41, 26.04, 24.83, 34.97, 45.37, 46.44, 40.33, 53.49, 59.06,
    56.8, 71.74, 62.64, 74.17, 83.96, 91.73, 81.33, 95.3, 106.5, 91.11, 90.05, 99.17, 117.5, 94.78, 67.07, 88.7, 104.7,
    93.82, 96.11, 107.8, 133.5, 123.8, 139.4, 164.4, 164.5, 207.3, 248.6, 241.0, 276.5, 348.6, 328.75, 388.51, 435.64,
    465.95, 455.19, 614.57, 743.25, 962.37, 1190.05, 1428.68, 1330.93, 1144.93, 899.18, 1080.64, 1199.21, 1262.07,
    1416.42, 1479.22, 877.56, 1110.38, 1241.53, 1243.32, 1422.29, 1807.78, 2054.27, 2054.08, 2246.63, 2664.34, 2567.31,
    3230.58, 3756.07, 4766.18, 4063.4,
)

dividends = (
    5.49, 5.92, 7.47, 7.27, 6.86, 8.38, 5.85, 5.22, 4.07, 4.45, 5.32, 5.48, 6.18, 7.14, 4.62, 3.9, 4.74, 4.47, 4.14,
    4.78, 4.07, 4.36, 5.67, 4.88, 4.4, 4.27, 3.79, 3.54, 3.49, 4.37, 4.03, 4.1, 5.33, 3.76, 3.46, 4.07, 6.7, 4.43, 4.27,
    5.19, 5.16, 5.12, 5.97, 5.71, 4.54, 5.71, 10.15, 7.22, 5.94, 7.49, 6.29, 5.81, 6.2, 5.41, 4.82, 5.11, 4.41, 3.67,
    4.53, 6.32, 9.72, 7.33, 4.41, 4.86, 3.6, 4.22, 7.26, 4.02, 5.01, 6.36, 8.11, 6.2, 5.31, 4.89, 3.81, 4.69, 5.59,
    6.12, 6.89, 7.44, 6.02, 5.41, 5.84, 4.4, 3.61, 3.75, 4.44, 3.27, 3.1, 3.43, 2.82, 3.4, 3.07, 2.98, 2.97, 3.53, 3.06,
    2.88, 3.47, 3.49, 3.1, 2.68, 3.57, 5.37, 4.15, 3.87, 4.98, 5.28, 5.24, 4.61, 5.36, 4.93, 4.31, 4.58, 3.81, 3.33,
    3.66, 3.53, 3.17, 3.68, 3.14, 2.84, 2.7, 2.89, 2.24, 2.0, 1.61, 1.36, 1.17, 1.22, 1.37, 1.79, 1.61, 1.62, 1.76,
    1.76, 1.87, 3.23, 2.02, 1.83, 2.13, 2.2, 1.94, 1.92, 2.11, 2.03, 1.84, 2.09, 1.83, 1.58, 1.29, 1.61,
)

print(len(prices), len(dividends))


def gains(
        year: int,
        prices, dividends,
        start_year: int, end_year: int,
        value: float = 1.,
        min_cap=-100., max_cap=100.,
        dividends_taxes=0.,
        add: float = 0.,
        echo=False,
        management_fee=0.,
):
    start = start_year - year
    end = end_year - year
    assert 0 <= start < end <= len(dividends) == len(prices) - 1

    assert -100. <= min_cap <= max_cap <= 100.
    # print 'years:', end-start
    contributed = value
    dividend_ratio = (100. - dividends_taxes) * 0.01
    for i in range(start, end):
        growth = 100. * prices[i + 1] / prices[i] - 100.
        annual = max(min(growth, max_cap), min_cap)
        # actual = annual + dividends[i] * dividend_ratio

        actual = (1. + annual * 0.01) * (1. + dividends[i] * dividend_ratio * 0.01) * 100. - 100.

        value = value * (1. + actual * 0.01)
        if echo:
            print(
                f'{i - start + 1:3}: {year + i}, {growth:6.2f}, {annual:6.2f}, {actual:6.2f}: {value:12,.2f}, {prices[i]:9,.2f}, {dividends[i]:4.2f}%')
            # .format(i - start + 1, year + i, growth, annual, actual, value, prices[i], dividends[i]))
        if i < end - 1:
            value += add
            contributed += add

        value = value * (1. - management_fee * 0.01)

    return value, contributed


def earnings(
        year: int,
        prices, dividends,
        start_year: int, end_year: int,
        min_cap=-100., max_cap=100.,
        dividends_taxes=0.,
        echo=False
):
    start = start_year - year
    end = end_year - year
    assert 0 <= start < end <= len(dividends) == len(prices) - 1

    assert -100. <= min_cap <= max_cap <= 100.
    # print 'years:', end-start
    dividend_ratio = (100. - dividends_taxes) * 0.01
    for i in range(start, end):
        growth = 100. * prices[i + 1] / prices[i] - 100.
        annual = max(min(growth, max_cap), min_cap)
        div = (1. + dividends[i] * dividend_ratio * 0.01) * 100. - 100.

        if echo:
            print(
                f'{i - start + 1:3}: {year + i}, {annual:6.2f}, {div:4.2f}%: {prices[i]:9,.2f}, {dividends[i]:4.2f}%')
            # .format(i - start + 1, year + i, growth, annual, actual, value, prices[i], dividends[i]))


# print len(prices), len(dividends)


def best_intervals(year, prices, dividends, first_year, last_year=2019, horizon=20, min_cap=0., max_cap=13., taxes=0.,
                   value0=1., add=0.):
    ind = 0
    for start_year in range(first_year, last_year - horizon + 1):
        end_year = start_year + horizon

        value1, c1 = gains(year, prices, dividends, start_year, end_year, value0, dividends_taxes=taxes, add=add)
        value1 = value1 - (value1 - value0 - add * (end_year - start_year - 1)) * taxes * 0.01
        value2, c2 = gains(year, prices, dividends, start_year, end_year, value0, min_cap, max_cap,
                           dividends_taxes=100., add=add)
        outperformed_ratio = value2 / value1
        if outperformed_ratio >= 1.01:
            ind += 1
            # print('{:3} {}-{}: ${:6.0f} vs ${:6.0f}, {:3.0f}%'.format(ind, start_year, end_year, value1, value2, outperformed_ratio * 100.-100.))
            r1 = CAGR(start_year, end_year, c1, value1)
            r2 = CAGR(start_year, end_year, c2, value2)
            dr = r2 - r1
            print(
                f'{ind:3} {start_year}-{end_year}: {money(value1):6} vs {money(value2):6}: {outperformed_ratio - 1:4.0%}, {r1:6.2%} vs {r2:6.2%}: {dr:6.2%}')


def test():
    start_year, end_year = 2019 - 20, 2019

    value0 = 1.
    value1 = gains(year, prices, dividends, start_year, end_year, value0)
    value2 = gains(year, prices, dividends, start_year, end_year, value0, 0., 13., 0.)
    # print value0, value1, value2


def test1():
    start_year, end_year = 1992, 2017

    value0 = 100000.
    value1 = gains(year, prices, dividends, start_year, end_year, value0, -100., 100., 0.)
    print(value1)
    value2 = gains(year, prices, dividends, start_year, end_year, value0, 0., 12.25, 100.)
    print(value2)
    print(value1 / value2)


def test2():
    start_year, end_year = 1997, 2019

    value0 = 100000.
    value1 = gains(year, prices, dividends, start_year, end_year, value0, -100., 100., 0., add=value0)
    print(value1)
    value2 = gains(year, prices, dividends, start_year, end_year, value0, 0., 12.25, 100., add=value0)
    print(value2)
    print(value1 / value2)


def test3():
    start_year, end_year = 1999, 2016

    value0 = 100000.
    value1 = gains(year, prices, dividends, start_year, end_year, value0, -100., 100., 0., add=0.)
    print(value1)
    value2 = gains(year, prices, dividends, start_year, end_year, value0, 0., 13., 100., add=0.)
    print(value2)
    print(value1 / value2)


def CAGR(start_year, end_year, start_value, end_value):
    years = end_year - start_year
    # growth = end_value - start_value
    rate = (float(end_value) / start_value) ** (1 / years) - 1.
    return rate


def test4():
    # best_intervals(year, prices, dividends, first_year=year, last_year=2019, horizon=30, min_cap=0., max_cap=13., taxes=15.+10.3)
    best_intervals(year, prices, dividends, first_year=year, last_year=2020, horizon=22, min_cap=0., max_cap=13.,
                   taxes=0., value0=1., add=1.)

    # test2()

    # test3()

    # best_intervals(year, prices, dividends, first_year=year, last_year=2020, horizon=17, min_cap=0., max_cap=13., taxes=0., value0=100000., add=0.)

    value = 1000.
    add = 0.
    # start_year, end_year = year, 2020
    start_year, end_year = 1972, 2020
    # start_year, end_year = 1987, 2020
    # start_year, end_year = 2000, 2020

    best_intervals(year, prices, dividends, first_year=start_year, last_year=end_year, horizon=25, min_cap=0.,
                   max_cap=12.,
                   taxes=0., value0=value, add=add)

    g500, c500 = gains(year, prices, dividends, start_year, end_year, value, min_cap=-100., max_cap=100.,
                       dividends_taxes=0., add=add, echo=False)

    gCap, cCap = gains(year, prices, dividends, start_year, end_year, value, min_cap=0., max_cap=12.,
                       dividends_taxes=100.,
                       add=add, echo=False)

    print(f'S&P-500: ${g500:,.0f}, CAGR: {CAGR(start_year, end_year, c500, g500):.2%}')
    print(f'IUL 12%: ${gCap:,.0f}, CAGR: {CAGR(start_year, end_year, cCap, gCap):.2%}')

    print(g500 / gCap, gCap / g500)

    value = 500000.
    start_year, end_year = 2002, 2015

    value = 10000.
    add = 10000.

    g500, c500 = gains(year, prices, dividends, start_year, end_year, value, min_cap=-100., max_cap=100.,
                       dividends_taxes=0., add=add, echo=True)

    gCap, cCap = gains(year, prices, dividends, start_year, end_year, value, min_cap=0., max_cap=14.,
                       dividends_taxes=100.,
                       add=add, echo=True)

    print(f'S&P-500: ${g500:,.0f}, CAGR: {CAGR(start_year, end_year, c500, g500):.2%}')
    print(f'IUL 12%: ${gCap:,.0f}, CAGR: {CAGR(start_year, end_year, cCap, gCap):.2%}')

    value = 100000.
    add = 0.
    start_year, end_year = 1998, 2017

    g500, c500 = gains(year, prices, dividends, start_year, end_year, value, min_cap=-100., max_cap=100.,
                       dividends_taxes=0., add=add, echo=True)

    gCap, cCap = gains(year, prices, dividends, start_year, end_year, value, min_cap=0., max_cap=12.5,
                       dividends_taxes=100.,
                       add=add, echo=True)

    print(f'S&P-500: ${g500:,.0f}, CAGR: {CAGR(start_year, end_year, c500, g500):.2%}')
    print(f'IUL 12%: ${gCap:,.0f}, CAGR: {CAGR(start_year, end_year, cCap, gCap):.2%}')


print('=' * 80)


def test5():
    value = 200000.
    add = 0.
    start_year, end_year = 2000, 2023

    g500, c500 = gains(year, prices, dividends, start_year, end_year, value, min_cap=-100., max_cap=100.,
                       dividends_taxes=0., add=add, echo=True, management_fee=0.10)

    gCap, cCap = gains(year, prices, dividends, start_year, end_year, value, min_cap=0., max_cap=13,
                       dividends_taxes=100., add=add, echo=True)

    print(f'S&P-500: ${g500:,.0f}, CAGR: {CAGR(start_year, end_year, c500, g500):.2%}')
    print(f'IUL 8%:  ${gCap:,.0f}, CAGR: {CAGR(start_year, end_year, cCap, gCap):.2%}')

    g500i, c500i = gains(year, prices, dividends, start_year, end_year, value, min_cap=-100., max_cap=100.,
                       dividends_taxes=100., add=add, echo=True, management_fee=0.10)
    print(f'Index:   ${g500i:,.0f}, CAGR: {CAGR(start_year, end_year, c500i, g500i):.2%}')

    earnings(year, prices, dividends, start_year, end_year, min_cap=-100., max_cap=100., dividends_taxes=0., echo=True)

    x = 1.1475 * (1. - 0.2058)
    g500 *= x
    g500i *= x
    print(f'S&P-500 Fund: ${g500:,.0f}, IUL: ${gCap:,.0f}, S&P-500 Index: ${g500i:,.0f}')


test5()
