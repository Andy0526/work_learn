# -*- coding: utf-8 -*-

import distance


def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)


strings = [
    '后来 我总算学会了如何去爱,可惜你早已远去消失在人海',
    '后来，我总算学会了如何去爱,可惜你早已远去，消失在人海。',
    '后来 我终于学会了如何去爱,可惜你早已远去消失在人海'
]

for s in strings:
    print edit_distance(s, '后来 我总算学会了如何去爱,可惜你早已远去消失在人海')
