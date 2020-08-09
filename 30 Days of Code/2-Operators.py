#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    #calculating tip
    tip = meal_cost * tip_percent/100
    #calcultating tax
    tax = meal_cost* tax_percent/100

    #total bil
    total_bil = meal_cost + tip + tax
    #round() funtion is used to print the integer value
    print(round(total_bil))


if __name__ == '__main__':
          
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)