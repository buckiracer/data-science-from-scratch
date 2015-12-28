from __future__ import division     #want 3/2 to == 1.5
import re, math, random             #regexes, maths functions, random numbers
import matplotlib.pyplot as plt     #pyplot
from collections import defaultdict, Counter
from functools import partial

def vector_add(v,w):
    """adds corresponding vectors"""
    return [v_i + w_i
            for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    """subtracts corresponding vectors"""
    return [v_i - w_i
            for v_i, w_i in zip(v,w)]

def vector_sums(vectors):
    return reduce(vector_add,vectors)

