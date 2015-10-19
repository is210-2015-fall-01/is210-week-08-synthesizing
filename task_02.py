#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week8 synthesizing task_02."""

DAY = raw_input('What day is it?: ')[:3].lower()

TIME = int(raw_input('What time is it?: '))

SNOOZE = True if (DAY == 'sat' or DAY == 'sun') or TIME < 600 else False

if SNOOZE is False:
    print 'Beep! ' * 5
