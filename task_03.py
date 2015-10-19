#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 03"""

import decimal

NAME = raw_input('What is your name? ')
PRCPL = int(raw_input('What is the principal of the loan? '))
TERM = int(raw_input('For how long is this being borrowed? '))
QUAL = raw_input('Are you pre-qualified? ').lower()[:1]

if QUAL == 'y':
    if PRCPL > 0 and PRCPL < 200000:
        if TERM >= 1 and TERM <= 15:
            INTRTE = decimal.Decimal('3.63')
        elif TERM > 15 and TERM <= 20:
            INTRTE = decimal.Decimal('4.04')
        elif TERM > 20 and TERM <= 30:
            INTRTE = decimal.Decimal('5.77')
        else:
            INTRTE = None
    elif PRCPL >= 200000 and PRCPL < 1000000:
        if TERM >= 1 and TERM <= 15:
            INTRTE = decimal.Decimal('3.02')
        elif TERM > 15 and TERM <= 20:
            INTRTE = decimal.Decimal('3.27')
        elif TERM > 20 and TERM <= 30:
            INTRTE = decimal.Decimal('4.66')
        else:
            INTRTE = None
    elif PRCPL >= 1000000:
        if TERM >= 1 and TERM <= 15:
            INTRTE = decimal.Decimal('2.05')
        elif TERM > 15 and TERM <= 20:
            INTRTE = decimal.Decimal('2.62')
        else:
            INTRTE = None
    else:
        INTRTE = None
elif QUAL == 'n':
    if PRCPL > 0 and PRCPL < 200000:
        if TERM >= 1 and TERM <= 15:
            INTRTE = decimal.Decimal('4.65')
        elif TERM > 15 and TERM <= 20:
            INTRTE = decimal.Decimal('4.98')
        elif TERM > 20 and TERM <= 30:
            INTRTE = decimal.Decimal('6.39')
        else:
            INTRTE = None
    elif PRCPL >= 200000 and PRCPL < 1000000:
        if TERM >= 1 and TERM <= 15:
            INTRTE = decimal.Decimal('3.98')
        elif TERM > 15 and TERM <= 20:
            INTRTE = decimal.Decimal('4.08')
        else:
            INTRTE = None
    else:
        INTRTE = None
else:
    INTRTE = None

if INTRTE is None:
    TOTAL = None
else:
    DEC_RT = decimal.Decimal(INTRTE) / 100
    TOTAL = int(round(PRCPL * ((1 + (DEC_RT / 12)) ** (12 * TERM))))

print ''
print 'Loan Report For: {}'.format(NAME)
print '-------------------------------------------'
print '      Principle:{:>15}'.format(PRCPL)
print '      Duration:{:>13}'.format(TERM)+' years'
print '      Pre-qualified?:{:>10}'.format(QUAL)
print ''
print '      Total:{:>19}'.format(TOTAL)
