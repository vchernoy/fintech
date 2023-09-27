death_ratesA = [5.92, 7.08, 8.52, 9.83, 11.23, 13.09, 16.01, 20.27, 26.65, 35.41, 45.45, 56.59, 69.12, 84.08, 101.37,
                121.64, 146.42, 173.99, 202.46, 232.64, 262.76, 289.78, 314.89, 341.11, 367.82, 393.73, 420.27, 446.33,
                472.99, 498.78, 523.83, 549.22, 574.33, 599.19, 623.95, 647.95, 670.95, 693.18, 713.89, 732.19, 748.82,
                762.44, 772.44, 778.24, 779.99, 777.18, 771.55, 762.55, 750.55, 735.95, 719.25, 701.35, 681.45, 659.44,
                635.29, 608.99, 579.75, 548.55, 516.55, 484.15, 451.55, 419.05, 386.95, 355.25, 324.25, 294.25, 266.05,
                240.29, 216.21, 194.44, 174.43, 155.96, 139.79, 125.17, 112.18, 100.44, 89.74, 80.28, 71.99, 64.76,
                58.38, 52.82, 47.97, 43.760, 40.150, 37.09, 34.550, 32.47, 30.79, 29.410, 28.35, 27.59, 27.150, 26.980,
                27.05, 27.32, 27.82, 28.560, 29.55, 30.78, 32.25, 33.97, 35.95, 38.18, 40.650, 43.36, 46.32, 49.52,
                52.96, 56.64, 60.550, 64.7, 69.10, 73.73, 78.59, 83.69, 89.01, 94.66, 100.64, 107.06, 113.79, 120.86,
                128.25, 135.96, 143.98, 152.32, 161.0, 170.01, 179.34, 188.98, ]

death_rates1 = [
    147.6, 166.2, 188.1, 200.5, 209.8, 223.5, 235.2, 248.5, 262.3, 278.5,
    293.8, 308.2, 324.3, 336.5, 354.3, 374.4, 395.2, 416.3, 443.2, 469.7,
    497.8, 527.2, 558.6, 590.7, 625.0, 660.4, 698.0, 736.6, 777.7, 819.9,
    862.9, 908.3, 955.2, 1001.7, 1050.0, 1101.7, 1153.3, 1207.3, 1262.8,
    1320.0, 1379.1, 1441.4, 1504.8, 1571.1, 1639.3, 1708.7, 1782.2, 1856.5,
    1934.1, 2014.5, 2096.8, 2182.9, 2271.1, 2362.8, 2456.8, 2553.3, 2652.1,
    2753.2, 2857.7, 2963.8, 3073.0, 3184.4, 3298.2, 3415.2, 3535.5, 3659.1,
    3785.9, 3915.9, 4049.1, 4185.5, 4325.0, 4467.8, 4613.7, 4763.0, 4915.3
]

death_ratesX = [104.1, 113.7, 125.6, 138.5, 152.2, 165.2, 170.7, 175.4, 180.0, 185.7, 189.3, 191.9, 192.1, 197.5, 204.7,
                213.8, 219.5, 228.1, 237.5, 249.2, 48.3, 54.2, 58.8, 65.1, 79.0, 94.2, 107.8, 124.4, 148.2, 177.8,
                214.1, 258.6, 312.3, 371.4, 442.2, 526.6, 622.6, 729.6, 862.6, 1032.6, 1103.8, 1308.7, 1557.8, 1858.7,
                2175.8, 2551.4, 2945.4, 3393.9, 3815.2, 4295.6, 4725.8, 5257.1, 5766.2, 6289.6, 6811.6, 7361.2, 7913.7,
                8552.4, 9219.5, 9898.7, 10614.6, 11371.2, 12190.7, 13117.6, 14090.2, 14966.9, 15889.8, 16924.3, 18018.5,
                19208.2, 20533.9, 21853.9, 23304.5, 24791.4, 26303.5, 27751.5, 29253.5, 30617.1, 32254.5, 33888.7,
                35516.8, 37205.9, 38772.8, 40368.1, 42062.3, 43715.3, 45522.9, 47179.9, 48962.8, 50832.7, 52802.1,
                54640.8, 56618.9, 58637.5, 60595.4, 62689.4, 64696.5, 66652.5, 68703.5, 70617.8, 72490.5, 74536.7,
                76395.2, 78420.9, 80369.8, 81913.7, 83728.3, 85174.3, 87020.9, 87985.2, 89576.7, 90392.6, 91115.8,
                92337.7, 92588.7, 92827.6, 92797.9, 93151.7, 93495.1, 93943.9, 94446.4, 95215.2, 96050.4, 97159.6,
                98431.9, 99839.3, 101506.3]
age_start = 20

# print(death_ratesX[40-age_start:40-age_start+20])

nonsmoking_death_rates2021 = [78.1, 81.5, 85.3, 87.2, 89.9, 100.7, 103.7, 107.9, 112.8, 116.7, 144.8, 152.3, 159.6,
                              168.9, 178.5, 229.3, 244.6, 260.7, 282.4, 308.1, 343.6]
age_start = 40
# print(nonsmoking_death_rates2021[40-age_start:40-age_start+20])


# smoking_death_rates2021 = [625.1, 866.7, 1265.5, 2002.5, 3047.3, 4585.7, 6435.5, 8902.8, 11703.5, 15196.7, 19670.1, 24977.4, 31415.6, 38638.7, 46704.6, 56205.9, 66154.6, 75949.7, 86205.6, 94650.4, 101461.6]
# age_start = 40
# print(smoking_death_rates2021[40-age_start:40-age_start+20])
#
#
# death_rates2021 = [393.6, 571.6, 868.7, 1389.9, 2227.9, 3382.8, 5012.7, 7161.1, 9784.4, 12800.4, 16544.7, 20707.3, 25190.3, 29788.8, 34621.7, 40111.4, 46192.3, 52808.3, 59020.7, 64638.9, 69732.9]
# age_start = 40
# print(death_rates[40-age_start:40-age_start+20])
#
#
# death_rates2019 = [387.4, 559.4, 847.7, 1359.9, 2157.5, 3281.1, 4841.8, 6923.3, 9457.9, 12388.7, 16050.4, 20149.4, 24550.4, 29013.7, 33725.8, 39028.5, 44785.5, 51069.7, 57105.2, 62695.1, 67747.3]
# age_start = 40
# print(death_rates2019[40-age_start:40-age_start+20])

nonsmoking_death_rates2019 = [76.3, 98.2, 141.1, 220.7, 333.9, 497.6, 718.7, 1001.6, 1346.2, 1757.9, 2239.7, 2778.1,
                              3376.5, 3977.8, 4569.7, 5142.2, 5688.2, 6203.3, 6693.7, 7139.9, 7539.1]
age_start = 40
# print(nonsmoking_death_rates2019[40-age_start:40-age_start+20])


# smoking_death_rates2019 = [593.9, 828.1, 1207.4, 1862.7, 2874.4, 4329.9, 6329.8, 8977.2, 12122.7, 15769.8, 20228.9, 25567.4, 31885.7, 38844.4, 46243.4, 54895.4, 63734.2, 72324.8, 79917.6, 85955.7, 90432.7]
# age_start = 40
# print(smoking_death_rates2019[40-age_start:40-age_start+20])


death_rates2019 = [112.4, 123.1, 129.8, 140.5, 155.7, 166.5, 182.3, 202.2, 218.5, 236.8, 260.5, 281.6, 305.9, 333.4,
                   364.4, 397.2, 433.2, 472.1, 516.8, 571.6, 616.7]
age_start = 40


class DeathRates:
    def __init__(self, age_start: int, death_rates: list[float]):
        self.age_start = age_start
        self.death_rates = tuple(death_rates)

    def __getitem__(self, age):
        if isinstance(age, slice):
            age = slice(age.start - self.age_start, age.stop - self.age_start, age.step)
            return self.death_rates[age]
        else:
            if age < self.age_start or age >= self.age_start + len(self.death_rates):
                raise IndexError(
                    f'{age} is invalid for death_rates aged {self.age_start} to {len(self.death_rates) + self.age_start}')

            return self.death_rates[age - self.age_start]


print(DeathRates(40, death_rates2019)[40:60])
print(DeathRates(40, nonsmoking_death_rates2021)[40:60])


def cost(death_rates: DeathRates, start_age: int, duration: int, death_benefit: float = 1000000,
         monthly_premium: float = 0, interest: float = 0, check: bool = False) -> float:
    total = 0
    for age in range(start_age, start_age + duration):
        death_rate = death_rates[age]
        annual_premium = death_benefit * death_rate / 100_000
        for month in range(12):
            if total < 0:
                total *= (1 + interest / 100) ** (1 / 12)
            total += annual_premium / 12
            total -= monthly_premium
            if check:
                if monthly_premium > 0 and total > 0:
                    print(total, age, month)

    return total


def cash_value_cost(death_rates: DeathRates, start_age: int, duration: int, death_benefit: float = 1000000,
                    monthly_premium: float = 0, interest: float = 0, check: bool = False) -> float:
    total = 0
    for age in range(start_age, start_age + duration):
        death_rate = death_rates[age]
        risk = death_benefit + total
        annual_premium = risk * death_rate / 100_000
        for month in range(12):
            if total < 0:
                total *= (1 + interest / 100) ** (1 / 12)
            total += annual_premium / 12
            total -= monthly_premium
            if check:
                if monthly_premium > 0 and total > 0:
                    print(total, age, month)

    return total


def test():
    death_rates = DeathRates(40, nonsmoking_death_rates2021)
    start_age = 40
    duration = 20
    death_benefit = 1_000_000

    print(start_age, death_rates[start_age], death_benefit * death_rates[start_age] / 100000 / 12)

    total = cost(death_rates, start_age, duration, death_benefit)
    print(f'{total=:.2f}')
    monthly_premium = total / duration / 12
    print(f'{monthly_premium=:.2f}')
    owe_if_pay = cost(death_rates, start_age, duration, death_benefit, monthly_premium)
    print(f'{owe_if_pay=:.2f}')
    interest = 3
    owe_if_pay_and_interest = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
    print(f'{owe_if_pay_and_interest=:.2f}')

    upper = monthly_premium
    lower = 0
    while abs(lower - upper) >= 0.01:
        monthly_premium = (lower + upper) * 0.5
        c = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
        if c < 0:
            upper = monthly_premium
        else:
            lower = monthly_premium

    print(f'{monthly_premium=:.2f}')
    cost_for_best_premium = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
    print(f'{cost_for_best_premium=:.2f}')


def readfile(filepath):
    """
    age,
    survived,
    dying during the year,
    probability of living,
    probability of dying,
    the number of person-years,
    total number of person-years,
    remaining years to live,
    the cumulative survival probability.
    """
    death_rates_male2010 = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                sec = line.split()
                age, live, dead, p_live, p_dead = int(sec[0]), int(sec[1]), int(sec[2]), float(sec[3]), float(sec[4])
                print(age, live, dead, p_live, round(p_dead * 100_000, 1))
                death_rates_male2010.append(round(p_dead * 100_000, 1))

    return death_rates_male2010


def readfile2(filepath):
    """
    age,
    survived,
    dying during the year,
    probability of living,
    probability of dying,
    the number of person-years,
    total number of person-years,
    remaining years to live,
    the cumulative survival probability.
    """
    death_rates2017 = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                sec = line.split()
                # print(sec)
                dead = float(sec[0])
                print(dead)
                death_rates2017.append(dead)

    return death_rates2017


death_rates2017 = DeathRates(0,
                             [577.7, 38.2, 24.8, 19.3, 14.9, 14.1, 12.6, 11.4, 10.4, 9.5, 9.3, 10.3, 13.3, 18.6, 25.8,
                              33.8, 42.1, 51.0, 60.3, 69.8, 79.5, 88.9, 97.0, 103.2, 108.0, 112.3, 116.5, 120.7, 125.2,
                              130.0, 135.1, 140.2, 145.4, 150.6, 155.6, 161.5, 167.9, 174.0, 179.8, 186.0, 193.6, 203.6,
                              216.0, 230.6, 247.0, 264.7, 284.6, 307.9, 335.7, 368.2, 403.0, 440.1, 482.0, 528.5, 577.8,
                              628.4, 679.4, 731.9, 786.9, 845.6, 909.3, 976.8, 1046.7, 1118.1, 1192.2, 1271.0, 1362.1,
                              1462.0, 1577.0, 1710.0, 1842.8, 2031.7, 2210.2, 2419.4, 2634.2, 2904.2, 3200.1, 3544.3,
                              3925.7, 4339.3, 4816.3, 5321.6, 5924.0, 6656.4, 7404.5, 8195.4, 9087.9, 10193.8, 11407.5,
                              12733.1, 14173.3, 15728.9, 17398.6, 19178.8, 21063.3, 23043.2, 25106.6, 27239.5, 29425.3,
                              31645.6, 100000.0])

death_rates_ca2020 = DeathRates(0, readfile2("./ca2020.txt"))


def test2():
    death_rates = DeathRates(0, readfile("./male_2010.txt"))
    death_rates = death_rates2017
    death_rates = death_rates_ca2020

    print(death_rates[0:101])
    print(death_rates[40:60])

    # death_rates = DeathRates(40, nonsmoking_death_rates2021)
    start_age = 40
    duration = 20
    death_benefit = 1_000_000

    print(start_age, death_rates[start_age], death_benefit * death_rates[start_age] / 100000 / 12)

    total = cost(death_rates, start_age, duration, death_benefit)
    print(f'total=${total:,.2f}')
    monthly_premium = total / duration / 12
    print(f'monthly_premium=${monthly_premium:.2f}')
    owe_if_pay = cost(death_rates, start_age, duration, death_benefit, monthly_premium)
    print(f'owe_if_pay=${owe_if_pay:,.2f}')
    interest = 5
    owe_if_pay_and_interest = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
    print(f'owe_if_pay_and_interest=${owe_if_pay_and_interest:,.2f}')

    upper = monthly_premium
    lower = 0
    while abs(lower - upper) >= 0.01:
        monthly_premium = (lower + upper) * 0.5
        c = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
        if c < 0:
            upper = monthly_premium
        else:
            lower = monthly_premium

    print(f'{monthly_premium=:.2f}')
    cost_for_best_premium = cost(death_rates, start_age, duration, death_benefit, monthly_premium, interest)
    print(f'{cost_for_best_premium=:.2f}')


test2()
