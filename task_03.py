# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03"""

import decimal

NAME = raw_input('What is your name? ')
P = int(raw_input('What is the amount of your principal? '))
T = int(raw_input('For how many years is this loan being borrowed? '))
PREQ = raw_input('Are you pre-qualified for this loan? ')

if 0 <= P <= 199999 and 1 <= T <= 15:
    if PREQ == 'Yes' or 'y':
        R = 3.63

    else:
        if PREQ == 'No' or 'N':
            R = 4.65

if 0 <= P <= 199999 and 16 <= T <= 20:
    if PREQ == 'Yes' or 'y':
        R = 4.04

    else:
        if PREQ == 'No' or 'N':
            R = 4.98

if 0 <= P <= 199999 and 21 <= T <= 30:
    if PREQ == 'Yes' or 'y':
        R = 5.77

    else:
        if PREQ == 'No' or 'N':
            R = 6.39

if 200000 <= P <= 999999 and 1 <= T <= 15:
    if PREQ == 'Yes' or 'y':
        R = 3.02

    else:
        if PREQ == 'No' or 'N':
            R = 3.98

if 200000 <= P <= 999999 and 16 <= T <= 20:
    if PREQ == 'Yes' or 'y':
        R = 3.27

    else:
        if PREQ == 'No' or 'N':
            R = 4.08

if 200000 <= P <= 999999 and 21 <= T <= 30:
    if PREQ == 'Yes' or 'y':
        R = 4.66

    else:
        if PREQ == 'No' or 'N':
            R = None

if P >= 1000000 and 1 <= T <= 15:
    if PREQ == 'Yes' or 'y':
        R = 2.05

    else:
        if PREQ == 'No' or 'N':
            R = None

else:
    if P >= 1000000 and 16 <= T <= 20:
        if PREQ == 'Yes' or 'y':
            R = 2.62
        elif PREQ == 'No' or 'N':
            R = None

REPORT = """Loan Report for: {0}
            Principal: ${1}
            Duration: {2}yrs
            Pre-qualified?: {3}
            Total: ${4}
        """
R = decimal.Decimal(R) / 100
TOTAL = int(round(P * ((1 + (R / 12)) ** (12 * T))))
FINAL = REPORT.format(NAME, P, T, PREQ, TOTAL)
print FINAL
