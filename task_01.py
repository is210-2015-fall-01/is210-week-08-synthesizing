#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A decision tree using raw input and nested if statements"""


BASE = raw_input('Which base color, "Seattle Grey" or "Manatee"?: ')
FINAL_SELECTION = 'Your selected colors are; {}, {} and {}.'


if BASE == 'Seattle Grey':
    ACCENT = raw_input('Which accent color, "Cumulus Nimbus" or\
                       "Ceramic Glaze"?: ')
    if ACCENT == 'Cumulus Nimbus':
        HILITE = raw_input('Which highlight color, "Off White" or\
                           "Paper White"?: ')
    else:
        HILITE = raw_input('Which highlight color, "Basically White" or\
                           "White"?: ')


else:
    ACCENT = raw_input('Which accent color, "Platinum Mist" or\
                       "Spartan Sage"?: ')
    if ACCENT == 'Platinum Mist':
        HILITE = raw_input('Which highlight color, "Bone White" or\
                           "Just White"?: ')
    else:
        HILITE = raw_input('Which highlight color, "Fractal White" or\
                           "Not White"?: ')
print FINAL_SELECTION.format(BASE, ACCENT, HILITE)
