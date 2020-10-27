#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for _ in range(1,11):
        print("{} x {} = {}".format(n,_,n*_))