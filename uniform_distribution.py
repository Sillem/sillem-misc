import sys
from scipy.stats import kstest, shapiro
import numpy as np
from math import cos, sin, log, sqrt, pi
### Moduł, który od zera generuje liczby pseudolosowe z rozkładu jednostajnego, a następnie przy użyciu Transformaty Box-Mullera uzyskujemy 
### zmienne losowe pochodzące z rozkładu normalnego (sprawdzone testem shapiro wilka)
class LinearCongrugentialGenerator(object):
    def __init__(self, a, c, m, seed=42):
        self.a = a
        self.c = c
        self.m = m 
        self.X = seed
        
    def generate_next(self):
        self.X = (self.a * self.X + self.c) % self.m
        return self.X

prng = LinearCongrugentialGenerator(1664525,1013904223,m=sys.maxsize)    
i = 1
sample_1 = []
sample_2 = []

first = prng.generate_next()
for j in range(100):
    next = prng.generate_next()
    sample_1.append(next/prng.m)
    i+=1
    if next == first:
        print(f'Generatorowi LCG o parametrach a={prng.a}, c={prng.c}, m={prng.m} wykonanie cyklu zajmuje {i} iteracji')
        break
    
for j in range(100):
    next = prng.generate_next()
    sample_2.append(next/prng.m)
    i+=1
    if next == first:
        print(f'Generatorowi LCG o parametrach a={prng.a}, c={prng.c}, m={prng.m} wykonanie cyklu zajmuje {i} iteracji')
        break
    
ks_stat, p_value_1 = kstest(np.array(sample_1), 'uniform', args=(0,1))
ks_stat, p_value_2 = kstest(np.array(sample_2), 'uniform', args=(0,1))
z1, z2 = [], []
for j in range(100):
    z1.append(sqrt(-2*log(sample_1[j])) * cos(2*pi*sample_2[j]))
    z2.append(sqrt(-2*log(sample_1[j])) * sin(2*pi*sample_2[j]))

shapiro_stat, p_value = shapiro(np.array(z1))
shapiro_stat, p_value = shapiro(np.array(z2))

print(p_value)