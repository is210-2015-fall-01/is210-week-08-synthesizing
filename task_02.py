#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm clock"""

DAYTODAY = raw_input("What day is it today? ")
DAYTODAY = DAYTODAY.lower()
DAYTODAY = DAYTODAY[0:3]
TIMENOW = raw_input("What time is it right now? (Please, no colon)")
TIMENOW = int(TIMENOW)

SNOOZE = (DAYTODAY == ('sat' or 'sun')) or (TIMENOW < 600)

if not SNOOZE:
    print 'Beep! Beep! Beep! Beep! Beep!'
