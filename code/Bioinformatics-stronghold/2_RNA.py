# rosalind_1_RNA
#
# Transcribing DNA into RNA
# https://rosalind.info/problems/rna/
#
# Given: A DNA string t having length at most 1000 nt.
# The transcribed RNA string of t.

#1
print(input().replace('T', 'U'))

#2
print(input().translate(str.maketrans('T','U')))

