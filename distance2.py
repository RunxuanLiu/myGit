# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:59:54 2017

@author: rickyliu
"""

import scipy as sp
from numpy import random
def point_to_surface(p11,p22,p33):
    p1 = p11
    p2 = p22
    #p3 = random.random(size=(10000000,3))
    p3 = p33
    dist = abs(sp.dot(p3-p1,sp.array(p2)-sp.array(p1))/sp.linalg.norm(sp.array(p1)-sp.array(p2)))
    
    return dist