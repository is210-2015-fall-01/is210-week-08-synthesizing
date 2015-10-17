#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A useful docstring."""

import decimal

NAME = raw_input('What is your name? ')
P = raw_input('What is the anmount of your principle? ')
T = raw_input('For how many years is the loan being borrowed? ')
PREQ = raw_input('Are you pre-qualified for this loan? ')
YES_PREQ = PREQ == 'Yes' or PREQ == 'y'
NO_PREQ = PREQ == 'No' or PREQ == 'n'
P = int(P)
T = int(T)
N = 12


def do_report(name, prin, years, preq, total):
    """Report Function.

    This function generates a report for the compounded interest fees.

    Args:
        name (str): Name of the customer
        prin (int): Principle
        years (int): Duration of loan
        preq (str): Pre-qualified status
        total (float): Total loan cost (principle + interest)

    Returns:
        report (str): A formatted report for the customer.

    Example:
        What is your name? Joe
        What is the anmount of your principle? 299334
        For how many years is the loan being borrowed? 20
        Are you pre-qualified for this loan? Yes
        Loan Report for: Joe
        --------------------------------------------------
        Principle:                    $299,334
        Duration:                     20yrs
        Pre-qualified?:               Yes

        Total:                        $575,172.817
"""
    report = 'Loan Report for: {}\n'.format(name)
    report += '-' * 50 + '\n'
    report += '\t{:<15} {:>15}{:,}\n'.format('Principle:', '$', prin)
    report += '\t{:<15} {:>15}{:>}\n'.format('Duration:', years, 'yrs')
    report += '\t{:<15} {:>15}\n\n'.format('Pre-qualified?:', preq)
    if TOTAL is None:
        report += '\t{:<15} {:>15}\n'.format('Total:', total)
    else:
        report += '\t{:<15} {:>15}{:,}\n'.format('Total:', '$', total)
    return report


if P >= 0 and P <= 199999:
    if T >= 1 and T <= 15:
        if YES_PREQ:
            R = 3.63
        elif NO_PREQ:
            R = 4.65
    elif T >= 16 and T <= 20:
        if YES_PREQ:
            R = 4.04
        elif NO_PREQ:
            R = 4.98
    elif T >= 21 and T <= 30:
        if YES_PREQ:
            R = 5.77
        elif NO_PREQ:
            R = 6.39
elif P >= 200000 and P <= 999999:
    if T >= 1 and T <= 15:
        if YES_PREQ:
            R = 3.02
        elif NO_PREQ:
            R = 3.98
    elif T >= 16 and T <= 20:
        if YES_PREQ:
            R = 3.27
        elif NO_PREQ:
            R = 4.08
    elif T >= 21 and T <= 30:
        if YES_PREQ:
            R = 4.66
        elif NO_PREQ:
            R = None
elif P >= 1000000:
    if T >= 1 and T <= 15:
        if YES_PREQ:
            R = 2.05
        elif NO_PREQ:
            R = None
    elif T >= 16 and T <= 20:
        if YES_PREQ:
            R = 2.62
        elif NO_PREQ:
            R = None
else:
    R = None
if R is None:
    TOTAL = None
else:
    TOTAL = long(round(decimal.Decimal(P * ((1+(decimal.Decimal(R/100)
                                           / N))**(N * T)))))
REPORT = do_report(NAME, P, T, PREQ, TOTAL)
print REPORT
