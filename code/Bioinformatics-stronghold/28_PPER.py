# rosalind_28_PPER
#
# Partial Permutations
# https://rosalind.info/problems/pper/
#
# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
# The total number of partial permutations P(n,k), modulo 1,000,000.

from math import factorial as fac

# P(n,k) // nPk

def pper(n: int, k: int):
    
    return fac(n) // fac(n-k)

    '''
    or
    result = 1 
    for i in range(k):
        result *= result -i
    '''
    
    
if __name__ == '__main__':
    
    with open('./datasets/rosalind_pper.txt') as inFile:
        n, k = map(int, inFile.readline().split())
            
    with open('./answers/rosalind_pper_outFile.txt', 'w') as outFile:        
        
       result = pper(n, k)
       print(f'{result%1000000}', file=outFile)
        
