#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 docstring"""

BASE = raw_input('Seattle Gray or Manatee?: ')
ACCENT = None
HIGHLIGHT = None

if BASE == 'Manatee':
    ACCENT = raw_input('Platinum Mist or Spartan Sage? ')
    if ACCENT == 'Spartan Sage':
        HIGHLIGHT = raw_input('Fractal White or Not White? ')
    elif ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Bone White or Just White? ')
elif BASE == 'Seattle Gray':
    ACCENT = raw_input('Ceramic Glaze or Cumulus Nimbus? ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Basically White or White? ')
    elif ACCENT == 'Cumulus Nimbus':
        HIGHLIGHT = raw_input('Off white or Paper White? ')

if HIGHLIGHT is None:
    PROMPT = 'Please complete your selection {}, {}, {}.'
    print PROMPT.format(BASE, ACCENT, HIGHLIGHT)
else:
    print 'Your selected colors are {}, {}, and {}.'\
          .format(BASE, ACCENT, HIGHLIGHT)
