# rosalind_25_LEXF
#
# Enumerating k-mers Lexicographically
# https://rosalind.info/problems/lexf/
#
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

#0) refer 12_PERM 

def lexf1(alpha_list, N):
    
    result = []
    
    if N == 0:      ### N == 1, return alpha_list 하면 더 낫다.
        return [[]]     # [[]]로 해야, 다음 구문에서 for 에서 none이 안나옴.
    
    for alpha in alpha_list:    # 'a', 'b', 'c' // [ ['a', 'a'], ['a', 'b'], ...]
        result.extend( [alpha] + word for word in lexf1(alpha_list, N-1) )
        
    return result

def lexf2(alpha_list, N):
    
    result = []
    
    if N == 1: 
        return alpha_list   # 이렇게 하면, 위에 꺼랑 달리 str concatenation으로 해결 가능.
    
    for alpha in alpha_list:    # 'a', 'b', 'c' // ['aa', 'ab' ...]
        result.extend( [alpha + word for word in lexf2(alpha_list, N-1)] )
    
    return result


if __name__ == '__main__':
    
    with open('./datasets/rosalind_lexf.txt') as inFile:
            
            alphabet = inFile.readline().split()
            N = int(inFile.readline())
        
    with open('./answers/rosalind_lexf_outFile.txt', 'w') as outFile:
        
        word_list = lexf1(alphabet, N)  # ['aa', 'ab', ..]
        for word in word_list: 
            print(''.join(word), file = outFile) 
        
'''other's solution

for p in it.product(alphabet,repeat=n):
    print ''.join(p)
    
k = 2
str = 'P R Q Z U A S N J D'
alphabet = str.split()
k_mer = alphabet

for  l in range(k-1):
    k_mer =  [i+j for i in alphabet for j in k_mer]

for i in k_mer: print i
'''
    
        
