
from numpy import random

def ripen(number_of_tomatoes):
    # generate random numbers following a normal distribution
    x = random.normal(loc=24.5, scale=2, size=number_of_tomatoes)
    return x