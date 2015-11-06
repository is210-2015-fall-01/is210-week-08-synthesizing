#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module helps you choose colors using if/else statements"""

BASESTR = 'Which base color, '
ACCENTSTR = 'Which accent color, '
HIGHLIGHTSTR = 'Which highlight color, '

BASE = raw_input(BASESTR + '"Seattle Gray" or "Manatee"? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input(ACCENTSTR + '"Ceramic Glaze" or "Cumulus Nimbus"? ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input(HIGHLIGHTSTR + '"Basically White" or White"? ')
    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input(HIGHLIGHTSTR + '"Off-White" or "Paper White"? ')
elif BASE == 'Manatee':
    ACCENT = raw_input(ACCENTSTR + '"Platinum Mist" or "Spartan Sage"? ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input(HIGHLIGHTSTR + '"Bone White" or "Just White"? ')
    elif ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input(HIGHLIGHTSTR + '"Fractal White" or "Not White"? ')
else:
    print '! The choices you entered are not valid. Please try again. !'

print 'Your selected colors are {}, {}, and {}.'.format(BASE, ACCENT, HIGHLIGHT)
