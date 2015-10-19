#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very basic alarm clock, using raw_input"""


DAY = raw_input('What day is it?: ').upper()
TIME = int(raw_input('What time is it?: '))
MY_TIME = 600

SNOOZE = (True if DAY[0:3] == ('SAT' or 'SUN') else False and MY_TIME < 600)

if SNOOZE == False:
    print 'Beep! '*5
