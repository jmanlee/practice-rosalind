# rosalind_3_REVC
#
# Complementing a Strand of DNA
# https://rosalind.info/problems/revc/
#
# Given: A DNA string s of length at most 1000 bp.
# The reverse complement sc of s.

print(input()[::-1].translate(str.maketrans('ATCG', 'TAGC')))
