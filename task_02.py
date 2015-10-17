#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A useful docstring."""

SNOOZE = False
ALARM = 'Beep! Beep! Beep! Beep! Beep!'
DAY = (raw_input('What day is it? '))[:3].lower()
TIME = raw_input('What time is it? ')
COMPARE = ((DAY == 'sat' or DAY == 'sun') or int(TIME) < 600)
SNOOZE = True if COMPARE else False
if SNOOZE is False:
    print ALARM
