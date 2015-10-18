#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A snoozing clock."""

MYDAY = raw_input('What day is it? \nEnter the day as Mon, Tue,' +
                  ' Wed, Thu, Fri, Sat, or Sun. \n--->>>  ')
MYTIME = raw_input('What time is it? \ne.g. Enter 8:15 AM as 0815 or 5:43 PM' +
                   ' as 1743.\n--->>>  ')

SNOOZE = True if (MYDAY == 'Sat' or MYDAY == 'Sun' or MYTIME < '0600') \
         else False

if SNOOZE:
    print 'Beep! Beep! Beep! Beep! Beep! Beep! Beep! Beep! Beep! Beep!'
