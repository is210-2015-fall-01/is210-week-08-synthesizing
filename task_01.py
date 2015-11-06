#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week8 synthesizing task_01 """


BASE = raw_input('Which base color, "{}" or "{}"?: '
                 .format('Seattle Gray', 'Manatee'))

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or "Cumulus '
                       'Nimbus" ')

else:
    ACCENT = raw_input('Which accent color "Platinum Mist" or "Spartan '
                       'Sage" ')

if ACCENT == 'Platinum Mist':
    HIGHLIGHT = raw_input('Which Highlight color, "Bone White" or "Just '
                          'White" ')

elif ACCENT == 'Spartan Sage':
    HIGHLIGHT = raw_input('Which Highlight color, "Fractal White" or "Not '
                          'White" ')

elif ACCENT == 'Cumulus Nimbus':
    HIGHLIGHT = raw_input('Which Highlight color, "Paper White" or "Off '
                          'White" ')

else:
    HIGHLIGHT = raw_input('Which Highlight color, "White" or "Basically '
                          'White" ')

MESSAGE = 'Your selected colors are {} {} {}'.format(BASE, ACCENT, HIGHLIGHT)

print MESSAGE
