'''Chemical Number Theory
Problem Description
A Mathematician and her husband, who is a professor of Chemistry, devise a game combining chemical element symbols and numbers to inspire children.

The husband provides the following list of 111 chemical elements:

List of elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg"]

Starting from H, whose atomic number is 1, till Rg, the atomic number increases by 1. Thus Rg has an atomic number of 111.

The wife provides the following table of number symbols and values:

Number symbol

Number face value

Smallest base using the symbol



The couple define "reactivity" of a chemical element by the equivalent smallest numeric value possible of its symbol. For example, here are the reactivities of a few elements:

Element

Reactivity

Remarks

H

17

The numeric value of H is 17

He

41*17+40 = 737

The smallest value possible is in base 41

L

21

The numeric value of L is 21

Be

41*11+40 = 491

The smallest value possible is in base 41

Au

10*57+56 = 626

The smallest value possible is in base 57

Two elements are said to have an "affinity" whose value is the HCF of their reactivities. For example, here are the affinities of a few pairs of elements:

Element 1

Reactivity of element 1

Element 2

Reactivity of element 2

Affinity of elements 1 and 2

Remarks

H

17

O

24

1

HCF of 17 and 24 is 1

Au

626

O

24

2

HCF of 626 and 24 is 2

Constraints
Maximum number of chemical symbols in the input: 10

Input
3 to 10 symbols of chemical elements from professor's list separated by spaces

Output
Print single integer which denotes the highest affinity amongst all pair of chemical elements provided in input.

Time Limit (secs)
1

Examples
Example 1

Input

H O C N Au Ag Cl

Output

12

Explanation

The affinities between each pair of elements are:

H-O: HCF of 17 and 24 is 1

H-C: HCF of 17 and 12 is 1

H-N: 1 (since the reactivity of H is 17. a prime)

H-Au: 1

H-Ag: 1

H-Cl: 1

O-C: HCF of 24 and 12 is 12

O-N: HCF of 24 and 23 is 1

O-Au: HCF of 24 and 626 is 2

O-Ag: HCF of 24 and 43*10+42 is 8

O-Cl: HCF of 24 and 48*12+47 is 1

C-N: HCF of 12 and 23 is 1

C-Au: HCF of 12 and 626 is 2

C-Ag: HCF of 12 and 472 is 4

C-Cl: HCF of 12 and 623 is 1

N-Au: HCF of 23 and 626 is 1

N-Ag: 1 (since the reactivity of N is 23. a prime)

N-Cl: 1

Au-Ag: HCF of 626 and 472 is 2

Au-Cl: HCF of 626 and 623 is 1

Ag-Cl: HCF of 472 and 623 is 1

Hence the maximum affinity is between O and C; the output is 12.

Example 2

Input

Tc S Be Li Er In Dy As I Ac

Output

7

Explanation

The maximum affinity is between Tc and S; hence, the output is 7.




'''
# def val(s):
    # if len(s)>1:
        # 
        # 
        # a=sym.index(s[0])
        # b=sym.index(s[1])
        # v=((b+1)*a)+(b)
        # return v
    # else:
# 
# 
        # 
        # v=sym.index(s)
        # return v
# 
# def isprime(s):
    # if s==1 or s==2:
        # return True
    # else:
        # for i in range(2,s):
            # if s%i==0:
                # return False
        # return True
#Function to find HCF the Using Euclidian algorithm
# def compute_hcf(x, y):
#    while(y):
    #    x, y = y, x % y
#    return x
# 
# 
# 
    # 
    # 
# 
# 
# 
# 
# 
# sym=["0","1","2","3","4","5","6","7","8","9",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# a=input()
# 
# a=list(a.split())
# k=[]
# hcf1=[]
# for i in a:
    # k.append(val(i))
# 
# for i in range(len(k)):
    # for j in range(i+1,len(k)):
        # if isprime(k[i]) or isprime(k[j]):
            # hcf1.append(1)
        # else:
            # hcf1.append(compute_hcf(k[i],k[j]))
# 
# 
# print(max(hcf1))

import math
knk="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
val={'0':[0,2]}
x=1
for c in knk[1:]:
    val[c]=[x,x+1]
    x+=1
l=input().split()
r={}
for x in l:
    reactivity=0
    if len(x)==1:
        reactivity=val[x][0]
    else:
        reactivity=val[x[1]][0]+val[x[0]][0]*val[x[1]][1]
    r[x]=reactivity
n=len(r)
if n==1:
    print(r[l[0]])
else:
    maxaff=1
    for x in l:
        for y in l:
            if x!=y:
                maxaff=max(maxaff,math.gcd(r[x],r[y]))
    print(maxaff)
