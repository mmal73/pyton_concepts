#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #n = int( input().strip() )
    for n in [ 1, 4, 6, 8, 21, 24 ]:
        res = ""
        if n%2 == 0 and ( n in range( 2, 6 ) or n > 20 ):
            res += "Not"
        res += "Weird"
        print( str( n ) + ": " + res )