# rosalind_14_PROB
#
# Introduction to Random Strings
# https://rosalind.info/problems/prob/
#
# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
# Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability 
# that a random string constructed with the GC-content found in A[k] will match s exactly.

from math import log10


def match_prob(seq: str, gc: float):

    """multiple each probability
    #1
    result = 1
    for nuc in seq:
        result *= gc/2 if nuc in ['G', 'C'] else (1-gc)/2

    return log10(result)
    """

    # 2 #log(x*y*z) = log(x) + log(y) + log(z)
    return sum( log10([(1 - gc) / 2, gc / 2][nuc in ["G", "C"]]) for nuc in seq )  # if nuc in GC True, index = 1, else False, index = 0


if __name__ == "__main__":

    with open("./datasets/rosalind_prob.txt") as inFile:

      s = inFile.readline().strip()  # DNA string
        A = list(map(float, inFile.readline().split()))  # gcContents

    with open("./answers/rosalind_prob_outFile.txt", "w") as outFile:

        for gc in A:
            print(f"{match_prob(s, gc)}", end=" ", file=outFile)

