# Copyright 2013 Luke Macken <lmacken@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Converts strings into unicode playing cards
"""

import sys

if sys.version_info.major == 3:
    unichr = chr

FACES = 'BA23456789TJCQKO'
UNICODE_FACES = '0123456789ABCDEF'
SUITS = 'SHDC'
UNICODE_SUITS = 'ABCD'
BACKS = ['', 'XX', 'YY', 'ZZ']

def unicard(card, color=False):
    if card[:2] == '10':
        card = 'T' + card[2]
    elif card[0] in FACES and card[1] in SUITS:
        face, suit = card.upper()
    else:
        face, suit = 'BS'
        
    c = unichr(int('0001f0%s%s' % (
            UNICODE_SUITS[SUITS.index(suit)],
            UNICODE_FACES[FACES.index(face)]
            ), base=16))
    return c

def tarot(card, color=False):
    rank = int(card)
    if rank == 22:
        rank = 0
    else:
        face, suit = 'BS'
        
    c = unichr(int('0001f0e0'), base=16) + rank
    return c