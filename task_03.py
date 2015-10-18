#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module calculates compound interest."""

import decimal

NMOS = 12
TOTAL = None

ANAME = raw_input('What is your name? ')
PRIN = int(raw_input('What is the principal amount? '))
SOMEYRS = int(raw_input('For how many years is this loan being borrowed? '))
PREQUAL = raw_input('Are you pre-qualified for this loan? ')

if PREQUAL == 'No' or PREQUAL == 'n':
    if 0 <= PRIN <= 199999:
        if 1 <= SOMEYRS <= 15:
            INTRATE = decimal.Decimal('0.0465')
        elif 16 <= SOMEYRS <= 20:
            INTRATE = decimal.Decimal('0.498')
        elif 21 <= SOMEYRS <= 30:
            INTRATE = decimal.Decimal('0.0639')
    elif 200000 <= PRIN <= 999999:
        if 1 <= SOMEYRS <= 15:
            INTRATE = decimal.Decimal('0.0398')
        elif 16 <= SOMEYRS <= 20:
            INTRATE = decimal.Decimal('0.0408')
elif PREQUAL == 'Yes' or PREQUAL == 'y':
    if 0 <= PRIN <= 199999:
        if 1 <= SOMEYRS <= 15:
            INTRATE = decimal.Decimal('0.0363')
        elif 16 <= SOMEYRS <= 20:
            INTRATE = decimal.Decimal('0.0404')
        elif 21 <= SOMEYRS <= 30:
            INTRATE = decimal.Decimal('0.0577')
    elif 200000 <= PRIN <= 999999:
        if 1 <= SOMEYRS <= 15:
            INTRATE = decimal.Decimal('0.0302')
        elif 16 <= SOMEYRS <= 20:
            INTRATE = decimal.Decimal('0.0327')
        elif 21 <= SOMEYRS <= 30:
            INTRATE = decimal.Decimal('0.0466')
    elif PRIN >= 1000000:
        if 1 <= SOMEYRS <= 15:
            INTRATE = decimal.Decimal('0.0205')
        elif 16 <= SOMEYRS <= 20:
            INTRATE = decimal.Decimal('0.0206')

TOTAL = PRIN * ((1 + INTRATE / NMOS) ** (NMOS * SOMEYRS))

REPORT = '''Loan Report for: {}
---------------------------------------------
    Principal:      ${:,}
    Duration:       {:>8}
    Pre-qualified?: {:>8}\n
    Total:          ${:,}'''

print REPORT.format(ANAME, PRIN, str(SOMEYRS) + ' yrs', PREQUAL, int(TOTAL))
