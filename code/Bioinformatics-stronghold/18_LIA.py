# rosalind_18_LIA
#
# Transcribing DNA into RNA
# Independent Alleles
#
# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
# Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
# Assume that Mendel's second law holds for the factors.

# When mated with genotype AaBb, no matter what genotype the organism has, the probability that the offspring is AaBb is always 1/4.

from math import factorial as fac

if __name__ == "__main__":

    with open("./datasets/rosalind_lia.txt") as inFile:
        k, N = map(int, inFile.readline().split())  # k generation, N AaBb

    with open("./answers/rosalind_lia_outFile.txt", "w") as outFile:

        K = 2 ** k
        prob = 0

        # binomial distrinution formula (K_Combination_N)
        for i in range(N, K + 1):
            p = ((fac(K)) / (fac(i) * fac(K - i))) * (0.25 ** i) * (0.75 ** (K - i))
            prob += p

        print(f"{prob:0.3f}", file=outFile)

