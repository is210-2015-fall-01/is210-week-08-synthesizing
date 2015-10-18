#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Caclulating mortgages"""


import decimal


NAME = raw_input("What is your name? ")
PRIN = raw_input("What is the amount of your principal? ")
PRIN = decimal.Decimal(PRIN)
DUR = raw_input("For how many years is this loan being borrowed? ")
DUR = decimal.Decimal(DUR)
PREQ_RAW = raw_input("Are you pre-qualified for this loan? ")
PREQ = PREQ_RAW.lower()
PREQ = PREQ[0]
IR = None


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
elif PRIN >= 1000000:
    if DUR >= 1 and DUR <= 15:
        if PREQ == 'y':
            IR = 2.05
    elif DUR >= 16 and DUR <= 20:
        if PREQ == 'y':
            IR = 2.62

if IR == None:
    IR = 0
    TOTAL = 'None'

IR = decimal.Decimal(IR)
IR = IR / 100
ONE = decimal.Decimal(1.0)
MONTH = decimal.Decimal(12.0)

TOTAL = int(round(PRIN * ((ONE + (IR / MONTH))**(MONTH * DUR))))
# TOTAL = (round(TOTAL)


REPORT = 'Loan Report for: {}\n\
--------------------------------------------------------------------\n\
\t{:<15} {:>12}\n\
\t{:<15} {:>12}\n\
\t{:<15} {:>12}\n\n\
\t{:<15} {:>12,}'



print REPORT.format(NAME, 'Principal:', PRIN, 'Duration:', str(DUR) + 'yrs', \
                    'Pre-Qualified?:', PREQ_RAW, 'Total:', TOTAL)

