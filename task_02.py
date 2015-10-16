#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple alarm clock with a snooze function."""

DAY1 = raw_input('What day is it?: ')
DAY2 = DAY1[:3]
DAY1 = DAY2.lower()
TIME1 = raw_input('What time is it? (4-digit number without colon): ')
TIME1 = int(TIME1)

if (DAY1 == 'sat' or 'sun') or TIME1 < 600:
    SNOOZE = True
else:
    print 'Beep! Beep! Beep! Beep! Beep!'
    SNOOZE = False
