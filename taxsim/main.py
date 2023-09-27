from dataclasses import dataclass
from enum import Enum


class FilingStatus(Enum):
    SINGLE = 1
    MARRIED_FILING_JOINTLY = 2
    MARRIED_FILING_SEPARATELY = 3
    HEAD_OF_HOUSEHOLD = 4


@dataclass
class TaxBracket:
    rate: float
    max: float


@dataclass
class TaxCredit:
    credit: float
    max: float


@dataclass
class TaxDesc:
    status: FilingStatus
    standard_deductions: float
    ordinary_income_rates: tuple[TaxBracket,...]
    longterm_capital_gains_rates: tuple[TaxBracket, ...]
    net_investment_income_rates: tuple[TaxBracket, ...]
    ctc: TaxCredit
    eitc: tuple[TaxCredit, ...]
    actc: float


@dataclass
class Taxpayer:
    status: FilingStatus
    dependents: int
    minor_dependents: int
    income: float
    unearned: float
    itemized_deductions: float

    def gross_income(self) -> float:
        return self.income + self.unearned

    def tax_deductions(self, tax: TaxDesc) -> float:
        return max(tax.standard_deductions, self.itemized_deductions)

    def agi(self, tax: TaxDesc) -> float:
        return max(self.gross_income() - self.tax_deductions(tax), 0)

    def federal_taxes(self, tax: TaxDesc) -> float:
        agi = self.agi(tax)
        taxes = 0
        for i in range(len(tax.ordinary_income_rates)):
            if i > 0:
                delta = min(agi, tax.ordinary_income_rates[i].max) - tax.ordinary_income_rates[i-1].max
            else:
                delta = min(agi, tax.ordinary_income_rates[i].max)

            if delta < 0:
                break
            taxes += delta * tax.ordinary_income_rates[i].rate

        return taxes

    def child_tax_credit(self, tax: TaxDesc) -> float:
        max_ctc = tax.ctc.credit
        if self.agi(tax) <= tax.ctc.max:
            amount = max_ctc
        else:
            amount = max(max_ctc - round((self.agi(tax) - tax.ctc.max) / 1000) * 50, 0)
        return amount * self.minor_dependents

    def unused_child_tax_credit(self, tax: TaxDesc) -> float:
        return max(self.child_tax_credit(tax) - self.federal_taxes(tax), 0)

    def additional_child_tax_credit(self, tax: TaxDesc) -> float:
        amount = max(
            min(max(self.agi(tax) - 2500, 0) * 0.15, self.unused_child_tax_credit(tax)),
            tax.actc * self.minor_dependents
        )
        return amount

    def earned_income_tax_credit(self, tax: TaxDesc) -> float:
        if self.minor_dependents > len(tax.eitc):
            credit = tax.eitc[-1]
        else:
            credit = tax.eitc[self.minor_dependents]
        return credit.credit if credit.max >= self.agi(tax) else 0

    def tax_owed(self, tax: TaxDesc):
        taxes = self.federal_taxes(tax)
        credits = min(self.child_tax_credit(tax), taxes) + self.additional_child_tax_credit(tax) + self.earned_income_tax_credit(tax)
        return taxes - credits


single = TaxDesc(
    status=FilingStatus.SINGLE,
    standard_deductions=13850,
    ordinary_income_rates=(
        TaxBracket(0.10, 11000),
        TaxBracket(0.12, 44725),
        TaxBracket(0.22, 95375),
        TaxBracket(0.24, 182100),
        TaxBracket(0.32, 231250),
        TaxBracket(0.35, 578125),
        TaxBracket(0.37, 10**20),
    ),
    longterm_capital_gains_rates=(
        TaxBracket(0.00, 44625),
        TaxBracket(0.15, 492300),
        TaxBracket(0.20, 10**20),
    ),
    net_investment_income_rates=(
        TaxBracket(0.00, 200000),
        TaxBracket(0.038, 10**20),
    ),
    ctc=TaxCredit(2000, 200000),
    eitc=(
        TaxCredit(600, 17640),
        TaxCredit(3995, 46560),
        TaxCredit(6604, 52918),
        TaxCredit(7430, 56838),
    ),
    actc=1600,
)

married_filing_jointly = TaxDesc(
    status=FilingStatus.MARRIED_FILING_JOINTLY,
    standard_deductions=27700,
    ordinary_income_rates=(
        TaxBracket(0.10, 22000),
        TaxBracket(0.12, 89450),
        TaxBracket(0.22, 190750),
        TaxBracket(0.24, 364200),
        TaxBracket(0.32, 462500),
        TaxBracket(0.35, 693750),
        TaxBracket(0.37, 10**20),
    ),
    longterm_capital_gains_rates=(
        TaxBracket(0.00, 89250),
        TaxBracket(0.15, 553850),
        TaxBracket(0.20, 10**20),
    ),
    net_investment_income_rates=(
        TaxBracket(0.00, 250000),
        TaxBracket(0.038, 10**20),
    ),
    ctc=TaxCredit(2000, 400000),
    eitc=(
        TaxCredit(600, 24210),
        TaxCredit(3995, 53120),
        TaxCredit(6604, 59478),
        TaxCredit(7430, 63398),
    ),
    actc=1600,
)

married_filing_separately = TaxDesc(
    status=FilingStatus.MARRIED_FILING_SEPARATELY,
    standard_deductions=13850,
    ordinary_income_rates=(
        TaxBracket(0.10, 11000),
        TaxBracket(0.12, 44725),
        TaxBracket(0.22, 95375),
        TaxBracket(0.24, 182100),
        TaxBracket(0.32, 231250),
        TaxBracket(0.35, 346875),
        TaxBracket(0.37, 10**20),
    ),
    longterm_capital_gains_rates=(
        TaxBracket(0.00, 44625),
        TaxBracket(0.15, 276900),
        TaxBracket(0.20, 10**20),
    ),
    net_investment_income_rates=(
        TaxBracket(0.00, 125000),
        TaxBracket(0.038, 10**20),
    ),
    ctc=TaxCredit(2000, 200000),
    eitc=(
        TaxCredit(600, 17640),
        TaxCredit(3995, 46560),
        TaxCredit(6604, 52918),
        TaxCredit(7430, 56838),
    ),
    actc=1600,
)


heads_of_household = TaxDesc(
    status=FilingStatus.HEAD_OF_HOUSEHOLD,
    standard_deductions=20800,
    ordinary_income_rates=(
        TaxBracket(0.10, 15700),
        TaxBracket(0.12, 59850),
        TaxBracket(0.22, 95375),
        TaxBracket(0.24, 182100),
        TaxBracket(0.32, 231250),
        TaxBracket(0.35, 578100),
        TaxBracket(0.37, 10**20),
    ),
    longterm_capital_gains_rates=(
        TaxBracket(0.00, 59750),
        TaxBracket(0.15, 523050),
        TaxBracket(0.20, 10**20),
    ),
    net_investment_income_rates=(
        TaxBracket(0.00, 200000),
        TaxBracket(0.038, 10**20),
    ),
    ctc=TaxCredit(2000, 200000),
    eitc=(
        TaxCredit(600, 17640),
        TaxCredit(3995, 46560),
        TaxCredit(6604, 52918),
        TaxCredit(7430, 56838),
    ),
    actc=1600,
)

taxpayer = Taxpayer(
    status=FilingStatus.SINGLE,
    dependents=0,
    minor_dependents=0,
    income=15000+single.standard_deductions,
    unearned=0,
    itemized_deductions=0,
)

print(taxpayer)
print(taxpayer.tax_deductions(single))
print(taxpayer.agi(single))
print(taxpayer.federal_taxes(single))
print(taxpayer.earned_income_tax_credit(single))
print(taxpayer.tax_owed(single))
