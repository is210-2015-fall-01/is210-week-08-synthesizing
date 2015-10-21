#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week8 synthesizing task_3"""

import decimal

NAME = raw_input('What is your Name? ')
PRINCIPAL = int(raw_input('What is the Ammount of your Principal? '))
YEARS = int(raw_input('For how many years is Loan borrowed? '))
PREQ = raw_input('Are you Pre-qualified? ').lower()
RATE = None
TOTAL = None
TERMS = 12

if 0 <= PRINCIPAL <= 199999:
    if 1 <= YEARS <= 15:
        if PREQ:
            RATE = '0.0363'
        else:
            RATE = '0.0465'
    elif 16 <= YEARS <= 20:
        if PREQ:
            RATE = '0.0404'
        else:
            RATE = '0.0498'
    elif 21 <= YEARS <= 30:
        if PREQ:
            RATE = '0.0577'
        else:
            RATE = '0.0639'
elif 200000 <= PRINCIPAL <= 999999:
    if 1 <= YEARS <= 15:
        if PREQ:
            RATE = '0.0302'
        else:
            RATE = '0.0398'
    elif 16 <= YEARS <= 20:
        if PREQ:
            RATE = '0.0327'
        else:
            RATE = '0.0408'
    elif 21 <= YEARS <= 30:
        if PREQ:
            RATE = '0.0466'
elif PRINCIPAL >= 1000000:
    if 0 < YEARS <= 15:
        if PREQ:
            RATE = '0.0205'
    if 16 <= YEARS <= 20:
        if PREQ:
            RATE = '0.0262'

if RATE is not None:
    RATE = decimal.Decimal(RATE)
    TOTAL = int(round(PRINCIPAL * ((1 + RATE / TERMS) ** (TERMS * YEARS))))

REPORT = """    Loan Report for: {}
----------------------------------------------------------------------------
----------------------------------------------------------------------------
                Principal: ${}
                Duration: {} Years
                Prequalified:{}
                Total: ${}
         """.format(NAME, PRINCIPAL, YEARS, PREQ, TOTAL)
print REPORT
