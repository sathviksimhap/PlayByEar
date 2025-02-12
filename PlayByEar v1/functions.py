from notes import *
from random import *

def get_scale(key):

    global nl
    scale = []
    i = nl.index(key)
    scale.append(nl[i])
    i += 2
    i %= 12
    scale.append(nl[i])
    i += 2
    i %= 12
    scale.append(nl[i])
    i += 1
    i %= 12
    scale.append(nl[i])
    i += 2
    i %= 12
    scale.append(nl[i])
    i += 2
    i %= 12
    scale.append(nl[i])
    i += 2
    i %= 12
    scale.append(nl[i])
    i += 1
    i %= 12

    return scale

def get_rand_scale():
    key = choice(nl)
    return get_scale(key)

