# rosalind_1_DNA
# https://rosalind.info/problems/dna/
#
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = input()
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))

# Other's solution
print(*map(input().count, "ACGT"))
print(*(s.count(nuc) for nuc in 'ACGT'))

