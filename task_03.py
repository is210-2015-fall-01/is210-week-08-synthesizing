#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Caclulating mortgages"""

# A=P(1+\frac{r}{n})^{nt}
import decimal

NAME = raw_input("What is your name? ")
PRIN = raw_input("What is the amount of your principal? ")
PRIN = int(PRIN)
DUR = raw_input("For how many years is this loan being borrowed? ")
DUR = int(DUR)
PREQ_RAW = raw_input("Are you pre-qualified for this loan? ")
PREQ = PREQ_RAW.lower()
PREQ = PREQ[0]


if PRIN >= 0 and PRIN <= 199999:
    if DUR >= 1 and DUR <= 15:
        if PREQ == 'y':
            IR = 3.63
        elif PREQ == 'n':
            IR = 4.65
    elif DUR >= 16 and DUR <= 20:
        if PREQ == 'y':
            IR = 4.04
        elif PREQ == 'n':
            IR = 4.98
    elif DUR >= 21 and DUR <= 30:
        if PREQ == 'y':
            IR = 5.77
        elif PREQ == 'n':
            IR = 6.39
elif PRIN >= 200000 and PRIN <= 999999:
    if DUR >= 1 and DUR <= 15:
        if PREQ == 'y':
            IR = 3.02
        elif PREQ == 'n':
            IR = 3.98
    elif DUR >= 16 and DUR <= 20:
        if PREQ == 'y':
            IR = 3.27
        elif PREQ == 'n':
            IR = 4.08
    elif DUR >= 21 and DUR <= 30:
        if PREQ == 'y':
            IR = 4.66
        elif PREQ == 'n':
            IR = None
elif PRIN >= 1000000:
    if DUR >= 1 and DUR <= 15:
        if PREQ == 'y':
            IR = 2.05
        elif PREQ == 'n':
            IR = None
    elif DUR >= 16 and DUR <= 20:
        if PREQ == 'y':
            IR = 2.62
        elif PREQ == 'n':
            IR = None
            
IR = decimal.Decimal(IR)
IR = IR / 100
PRIN = decimal.Decimal(PRIN)
DUR = decimal.Decimal(DUR)
ONE = decimal.Decimal(1)
MONTHS = decimal.Decimal(12)

TOTAL = decimal.Decimal(PRIN * (1 + (IR / 12))**(12 * DUR))
TOTAL = int(round(TOTAL))

REPORT = 'Loan Report for: {}\n\
--------------------------------------------------------------------\n\
\t{:<15} {:>12,}\n\
\t{:<15} {:>12}\n\
\t{:<15} {:>12}\n\n\
\t{:<15} {:>12,}'



print REPORT.format(NAME, 'Principal:', PRIN, 'Duration:', str(DUR) + 'yrs', \
                    'Pre-Qualified?:', PREQ_RAW, 'Total:', TOTAL)

