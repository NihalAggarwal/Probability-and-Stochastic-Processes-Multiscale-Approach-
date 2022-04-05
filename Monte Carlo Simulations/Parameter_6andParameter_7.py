import numpy as np
import math 
import random
import matplotlib.pyplot as plt
from scipy.stats import poisson
import pandas as pandas
from scipy.stats import uniform
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad


### This is just Monte Crlo Simulations for Parameter 6 and 7 which were discussed in the paper that they were ###
### conducted to just cross checkl results, They are not used for drawing any inferences such but just for validating and SIMULATING MONTE CARLO TO ###
### Enchance our understanding of the Same ###

n= 100
start = 0.04
width = 0.08
Nr = uniform.rvs(size=n, loc = start, scale=width)
Lambda=0.25 
### Probability of SSB converting to a Double Strand Break after ###

LC =Lambda*(1-poisson.pmf(1,Nr)-poisson.pmf(0,Nr)-poisson.pmf(2,Nr))

LCvalue=0
for i in LC:
    LCvalue+=i

print("The critical Value is ")
print(LCvalue)


def Nr(num):
    return num
    # LeCrit =Lambda*(1-poisson.pmf(1,num)-poisson.pmf(0,num)-poisson.pmf(2,num))
    # return LC

Nrrandom=[]
samplist11=[]
samplistLC=[]
def MonteCarlo(n):
    results=0
    for i in range(n):
        a=random.uniform(0.04,0.08)
        Nrrandom.append(a)
        Nr_results=Nr(a)
        results+=Nr_results
        prob=results/(i+1)
        samplist11.append(prob)

    plt.ylabel("The estimated value of Nr analyse")
    plt.xlabel("Number of iterations")
    plt.plot(samplist11)
    plt.show()
    return (results/n)

answer=MonteCarlo(100)

print("Monte Carlo Analysis Analysis for Paramter 6 ---> Nr")
print (answer)

num=0.05
LeCrit =Lambda*(1-poisson.pmf(1,num)-poisson.pmf(0,num)-poisson.pmf(2,num))
print(LeCrit)
print("Lethality criterion check")

def LC(num):
    
    LeCrit =Lambda*(1-poisson.pmf(1,num)-poisson.pmf(0,num)-poisson.pmf(2,num))
    return LeCrit

Nrrandom1=[]
samplist12=[]
samplistLC=[]
def MonteCarlo1(n):
    results=0
    for i in range(n):
        a=random.uniform(0.04,0.08)
        Nrrandom1.append(a)
        LC_results=LC(a)
        results+=LC_results
        prob=results/(i+1)
        samplistLC.append(prob)

    plt.ylabel("Value of Lehtality Criterion")
    plt.xlabel("Number of iterations")
    plt.plot(samplistLC)
    plt.show()
    return (results/n)

answer=MonteCarlo1(100)

print("Monte Crlo Analysis for Paramter 6 ---> Lethality Crtieria Pl(l)")
print (answer)



