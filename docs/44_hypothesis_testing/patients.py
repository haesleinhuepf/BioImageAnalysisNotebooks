
from numpy import random

def placebo_group(number_of_patients):
    # generate random numbers following a normal distribution
    x = random.normal(loc=7, scale=2, size=number_of_patients)
    return x

def treatment_group(number_of_patients):
    # generate random numbers following a normal distribution
    x = random.normal(loc=7, scale=2, size=number_of_patients)
    return x
