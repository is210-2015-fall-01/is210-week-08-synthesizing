#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A decision tree using raw input and nested if statements"""


import decimal
C_FLAG = True

NAME = raw_input('What is your name?: ')
PRIN = int(raw_input('What is the PRINcipal of the loan?: '))
YEAR = int(raw_input('How long is this being borrowed?: '))
PRE_Q_RAW = raw_input('Are you pre-qualified?: ')


if PRE_Q_RAW.upper() in ['YES', 'Y']:
    PRE_Q = True
elif PRE_Q_RAW.upper() in ['NO', 'N']:
    PRE_Q = False
else:
    C_FLAG = False
n = 12

if PRIN > 0 and PRIN <= 199999:
    if YEAR > 0 and YEAR <= 15:
        if PRE_Q is True:
            I_RATE = 3.63
        else:
            I_RATE = 4.65
    elif YEAR > 15 and YEAR <= 20:
        if PRE_Q is True:
            I_RATE = 4.04
        else:
            I_RATE = 4.98
    elif YEAR > 20 and YEAR <= 30:
        if PRE_Q is True:
            I_RATE = 5.77
        else:
            I_RATE = 6.39
    else:
        C_FLAG = False
elif PRIN >= 200000 and PRIN <= 999999:
    if YEAR > 0 and YEAR <= 15:
        if PRE_Q is True:
            I_RATE = 3.02
        else:
            I_RATE = 3.98
    if YEAR > 15 and YEAR <= 20:
        if PRE_Q is True:
            I_RATE = 3.27
        else:
            I_RATE = 4.08
    if YEAR > 20 and YEAR <= 30:
        if PRE_Q is True:
            I_RATE = 4.66
        else:
            C_FLAG = False
    else:
        C_FLAG = False
elif PRIN >= 1000000:
    if YEAR > 0 and YEAR <= 15:
        if PRE_Q is True:
            I_RATE = 2.05
        else:
            C_FLAG = False 
    if YEAR > 15 and YEAR <= 20:
        if PRE_Q is True:
            I_RATE = 2.62
        else:
            C_FLAG = False
    else:
        C_FLAG = False    
else:
    C_FLAG = False

if C_FLAG is True:
    TOTAL = PRIN * (1 + (I_RATE / n))**(n * YEAR)
else:
    TOTAL = None
print TOTAL

REPORT = "Loan Report for: {}\n" + \
"----------------------------------------------------------------------\n" + \
"\t PRINcipal:${:30,d}\n" + \
"\t Duration:{:30d}yrs\n" + \
"\t Pre-qualified:{:>30}\n" + \
"\t Total:${:>20,f}"
print REPORT.format(NAME, PRIN, YEAR, PRE_Q_RAW,(decimal.Decimal(TOTAL), -1))
