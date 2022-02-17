# rosalind_29_RSTR
#
# Matching Random Motifs
# https://rosalind.info/problems/rstr/
#
# Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
# Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x 
# (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.

    
from operator import mul
from functools import reduce


if __name__ == '__main__':
    
    with open('./datasets/rosalind_rstr.txt') as inFile:
        n, GC = inFile.readline().split()
        DNA = inFile.readline().strip()
        
    with open('./answers/rosalind_rstr_outFile.txt', 'w') as outFile:        
        
        n = int(n)
        GC = float(GC)

        #probability of emerging DNA
        p = 1
        for s in DNA:
           p *= (GC/2) if s in 'GC' else ((1-GC)/2)
           
        #2 solution
        p2 = reduce(mul, [[(1-GC)/2, GC/2][nuc in 'GC'] for nuc in DNA], 1)
        
        #binomial distribution // 1 - probability of never DNA string s
        result = (1 - (p**0)*(1-p)**n)
       
        print(f'{result}', file=outFile)
