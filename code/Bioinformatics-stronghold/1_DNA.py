# rosalind_1_DNA
# https://rosalind.info/problems/dna/

s = input()
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))

#참고할 풀이 *사용이 또 나왔네
print(*map(input().count, "ACGT"))
print(*(s.count(nuc) for nuc in 'ACGT'))
