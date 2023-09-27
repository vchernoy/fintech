year = 1871

prices = (4.44, 4.86, 5.11, 4.66, 4.54, 4.46, 3.55, 3.25, 3.58, 5.11, 6.19, 5.92, 5.81, 5.18, 4.24, 5.2, 5.58, 5.31, 5.24, 5.38, 4.84, 5.51, 5.61, 4.32, 4.25, 4.27, 4.22, 4.88, 6.08, 6.1, 7.07, 8.12, 8.46, 6.68, 8.43, 9.87, 9.56, 6.85, 9.06, 10.08, 9.27, 9.12, 9.3, 8.37, 7.48, 9.33, 9.57, 7.21, 7.85, 8.83, 7.11, 7.3, 8.9, 8.83, 10.58, 12.65, 13.4, 17.53, 24.86, 21.71, 15.98, 8.3, 7.09, 10.54, 9.26, 13.76, 17.59, 11.31, 12.5, 12.3, 10.55, 8.93, 10.09, 11.85, 13.49, 18.02, 15.21, 14.83, 15.36, 16.88, 21.21, 24.19, 26.18, 25.46, 35.6, 44.15, 45.43, 41.12, 55.62, 58.03, 59.72, 69.07, 65.06, 76.45, 86.12, 93.32, 84.45, 95.04, 102.0, 90.31, 93.49, 103.3, 118.4, 96.11, 72.56, 96.86, 103.8, 90.25, 99.71, 110.9, 133.0, 117.3, 144.3, 166.4, 171.6, 208.2, 264.5, 250.5, 285.4, 339.97, 325.49, 416.08, 435.23, 472.99, 465.25, 614.42, 766.22, 963.36, 1248.77, 1425.59, 1335.63, 1140.21, 895.84, 1132.52, 1181.41, 1278.73, 1424.16, 1378.76, 865.58, 1123.58, 1282.62, 1300.58, 1480.4, 1822.36, 2028.18, 1918.6, 2275.12, 2789.8, 2607.39, 3044.02)

dividends = (5.49, 5.92, 7.47, 7.27, 6.86, 8.38, 5.85, 5.22, 4.07, 4.45, 5.32, 5.48, 6.18, 7.14, 4.62, 3.9, 4.74, 4.47, 4.14, 4.78, 4.07, 4.36, 5.67, 4.88, 4.4, 4.27, 3.79, 3.54, 3.49, 4.37, 4.03, 4.1, 5.33, 3.76, 3.46, 4.07, 6.7, 4.43, 4.27, 5.19, 5.16, 5.12, 5.97, 5.71, 4.54, 5.71, 10.15, 7.22, 5.94, 7.49, 6.29, 5.81, 6.2, 5.41, 4.82, 5.11, 4.41, 3.67, 4.53, 6.32, 9.72, 7.33, 4.41, 4.86, 3.6, 4.22, 7.26, 4.02, 5.01, 6.36, 8.11, 6.2, 5.31, 4.89, 3.81, 4.69, 5.59, 6.12, 6.89, 7.44, 6.02, 5.41, 5.84, 4.4, 3.61, 3.75, 4.44, 3.27, 3.1, 3.43, 2.82, 3.4, 3.07, 2.98, 2.97, 3.53, 3.06, 2.88, 3.47, 3.49, 3.1, 2.68, 3.57, 5.37, 4.15, 3.87, 4.98, 5.28, 5.24, 4.61, 5.36, 4.93, 4.31, 4.58, 3.81, 3.33, 3.66, 3.53, 3.17, 3.68, 3.14, 2.84, 2.7, 2.89, 2.24, 2.0, 1.61, 1.36, 1.17, 1.22, 1.37, 1.79, 1.61, 1.62, 1.76, 1.76, 1.87, 3.23, 2.02, 1.83, 2.13, 2.2, 1.94, 1.92, 2.11, 2.03, 1.84, 2.09, 1.88)


def compute1(year: int, prices: tuple, dividends: tuple, beg: int, horizon: int, threshold: float) -> None:
    beg -= year
    end = beg + horizon
    assert 0 <= beg < end <= len(prices)
    prices = prices[beg:end+1]
    dividends = dividends[beg:end]
    growth = [100.*prices[i+1]/prices[i] for i in range(len(prices)-1)]
    print(' '.join(f'{p:.2f}' for p in growth))
    print(' '.join(f'{p:.2f}' for p in dividends))
    tot_growth = tuple(growth[i] + dividends[i] for i in range(horizon))
    print(' '.join(f'{p:.2f}' for p in tot_growth))
    selected = tuple(tot_growth[i] for i in range(len(tot_growth)) if tot_growth[i] >= threshold)
    print(selected)
    average = sum(selected) / len(selected)
    print(average)


def compute(year, prices, dividends, beg, horizon, threshold):
    beg -= year
    end = beg + horizon
    assert 0 <= beg < end <= len(prices)
    prices = prices[beg:end + 1]
    dividends = dividends[beg:end]
    growth = tuple(100. * prices[i + 1] / prices[i] for i in range(len(prices) - 1))
    print(growth)
    print(dividends)
    tot_growth = tuple(growth[i] + dividends[i] for i in range(horizon))
    print(tot_growth)
    selected = tuple(tot_growth[i] for i in range(len(tot_growth), 1) if tot_growth[i - 1] >= threshold)
    average = sum(selected) / len(selected)


compute(year, prices, dividends, 2020-20, 20, 120)

