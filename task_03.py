#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a mortgage calculator. Lifetime compound interest of loan."""

import decimal


NAME = raw_input('What is your name? ')
PRINC = int(raw_input('What is the amount of your principal? '))
DURAT = int(raw_input('For how many years is this loan being borrowed? '))
PREQU = raw_input('Are you pre-qualified for this loan? ')
PREQU1 = PREQU[:1]
PREQU2 = PREQU1.upper()[:1]

if PRINC < 199999:
    if DURAT <= 15:
        if PREQU2 == 'Y':
            INTRAT = decimal.Decimal('3.63')
        else:
            INTRAT = decimal.Decimal('4.65')
    elif 16 <= DURAT and DURAT <= 20:
        if PREQU2 == 'Y':
            INTRAT = decimal.Decimal('4.04')
        else:
            INTRAT = decimal.Decimal('4.98')
    elif 21 <= DURAT and DURAT <= 30:
        if PREQU2 == 'Y':
            INTRAT = decimal.Decimal('5.77')
        else:
            INTRAT = decimal.Decimal('6.39')
    else:
        INTRAT = None

elif 200000 <= PRINC and PRINC <= 999999:
    if DURAT <= 15:
        if PREQU2 == 'Y':
            INTRAT = decimal.Decimal('3.02')
        else:
            INTRAT = decimal.Decimal('3.98')
    elif 16 <= DURAT and DURAT <= 20:
        if PREQU2 == 'Y':
            INTRAT = decimal.Decimal('3.27')
        else:
            INTRAT = decimal.Decimal('4.08')
    elif DURAT >= 21 and PREQU2 == 'Y':
        INTRAT = decimal.Decimal('4.66')
    else:
        INTRAT = None  

elif PRINC >= 1000000 and PREQU2 == 'Y':
    if DURAT <= 15:
        INTRAT = decimal.Decimal('2.05')
    elif 16 <= DURAT and DURAT <= 20:
        INTRAT = decimal.Decimal('2.62')
    else:
        INTRAT = None


if INTRAT is None:
    TOTAL = None
else:
    INTRAT2 = decimal.Decimal(INTRAT) / 100
    TOTAL = int(round(PRINC * ((1 + (INTRAT2 / 12)) ** (DURAT * 12))))
REPORT = 'Loan Report for: {}'.format(NAME)
RPRINC = '      Principal:          ${:>2}'.format(PRINC)
RDURAT = '      Duration:  {:>13}yrs'.format(DURAT)
RPREQU = '      Pre-qualified?: {:>11}'.format(PREQU)
RTOTAL = '      Total               ${:>5}'.format(TOTAL)

print ''
print REPORT
print '-' * 50
print RPRINC
print RDURAT
print RPREQU
print RTOTAL
