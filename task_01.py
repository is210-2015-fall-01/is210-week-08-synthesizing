#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A useful docstring."""

WBC = 'Which base color'
WAC = 'Which accent color'
WHC = 'Which highlight color'

BASE = raw_input('{}, "Seattle Gray" or "Manatee"? '.format(WBC))
if BASE == 'Seattle Gray':
    ACCENT = raw_input('{}, "Ceramic Glaze" or "Cumulus nimbus"? '.format(WAC))
    if ACCENT == 'Ceramic Glaze':
        HL = raw_input('{}, "Basically White" or "White"? '.format(WHC))
    elif ACCENT == 'Cumulus Nimbus':
        HL = raw_input('{}, "Off-White" or "Paper White"? '.format(WHC))
elif BASE == 'Manatee':
    ACCENT = raw_input('{}, "Platinum Mist" or "Spartan Sage"? '.format(WAC))
    if ACCENT == 'Platinum Mist':
        HL = raw_input('{}, "Bone White" or "Just White"? '.format(WHC))
    elif ACCENT == 'Spartan Sage':
        HL = raw_input('{}, "Fractal White" or "Not White"? '.format(WHC))
HIGHLIGHT = HL
MESSAGE = 'Your selection colors are {}, {}, and {}'
print MESSAGE.format(BASE, ACCENT, HIGHLIGHT)
