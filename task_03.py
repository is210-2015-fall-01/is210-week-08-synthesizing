#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a mortgage calculator. Lifetime compound interest of loan."""


NAME = raw_input('What is your name? ')
PRINC = raw_input('What is the amount of your principal? ')
PRINC = int(PRINC)
DURAT = raw_input('For how many years is this loan being borrowed? ')
DURAT = int(DURAT)
PREQU = raw_input('Are you pre-qualified for this loan? ')
PREQU1 = PREQU[:1]
PREQU2 = PREQU1.upper()

if PRINC < 199999:
    if DURAT <= 15:
        if PREQU2 == 'Y':
            intrate = .0363
        else:
            intrate = .0465
    elif 16 <= DURAT and DURAT <= 20:
        if PREQU2 == 'Y':
            intrate = .0404
        else:
            intrate = .0498
    else:
        if PREQU2 == 'Y':
            intrate = .0577
        else:
            intrate = .0639

elif 200000 <= PRINC and PRINC <= 999999:
    if DURAT <= 15:
        if PREQU2 == 'Y':
            intrate = .0302
        else:
            intrate = .0398
    elif 16 <= DURAT and DURAT <= 20:
        if PREQU2 == 'Y':
            intrate = .0327
        else:
            intrate = .0408
    if DURAT >= 21 and PREQU2 == 'Y':
        intrate = .0466

elif PRINC >= 1000000 and PREQU2 == 'Y':
    if DURAT <= 15:
        intrate = .0205
    elif 16 <= DURAT and DURAT <= 20:
        intrate = .0262
else:
    TOTAL = None

TOTAL = PRINC*(1 + float((float(intrate)/12))**(DURAT*12))
TOTAL = int(TOTAL)
print PRINC
print DURAT
print PREQU
print TOTAL


#REPORT = "'Loan Report for: {}'.format(NAME)
#'-' * 50
# 'Principal: ${}'.format(PRINC)
# 'Duraction: {}yrs'.format{DURAT}
# 'Pre-qualified?: {}'.format{PREQU}
#
# 'Total: $'.format()"
#print REPORT
