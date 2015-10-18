#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w8 synthesizing task 02."""

DAY = raw_input('What day is it? ').strip().lower()[:3]
TIME = int(raw_input('What time is it? '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if not SNOOZE:
    print ('Beep! '*5).strip()
