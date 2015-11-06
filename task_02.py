#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm clock"""

DAY = raw_input('What day is it?: ')[:3].lower().strip()
TIME = int(raw_input('What time is it? (please provide military time): '))

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 600 else False

if not SNOOZE:
    print 'Beep! Beep! Beep! Beep! Beep!'
