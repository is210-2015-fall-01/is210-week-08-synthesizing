# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Using raw_input"""

BASE = raw_input('Which base color, Seattle Gray or Manatee? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('Which accent color, Ceramic Glaze or'
                       'Cumulus Nimbus? ')

    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color, Basically White'
                              'or White? ')
    else:
        HIGHLIGHT = raw_input('Which highlight,Off white or Paper White? ')

else:
    ACCENT = raw_input('Which accent color,Platinum Mist or Spartan Sage?')

    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight,Bone White or Just White? ')

    else:
        HIGHLIGHT = raw_input('Which highlight color, Fractal White'
                              'or Not White? ')

SELECTED = 'You selected {}, {} and {}'.format(BASE, ACCENT, HIGHLIGHT)
