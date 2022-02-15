# rosalind_7_IPRB
#
# Mendel's First Law
# https://rosalind.info/problems/iprb/
#
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
# (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


if __name__ == "__main__":

    with open("./datasets/rosalind_iprb.txt", "r") as inFile:
        # AA Aa aa
        k, m, n = map(int, inFile.readline().split())
        total = k + m + n

        # Aa*Aa / Aa*aa (2 case) / aa*aa
        homo_recessive = (
            0.5 * (m / total) * 0.5 * ((m - 1) / (total - 1))
            + 2 * 0.5 * (m / total) * (n / (total - 1))
            + (n / total) * ((n - 1) / (total - 1))
        )

    with open("./answers/roslaind_iprb_outFile.txt", "w") as outFile:
        print(1 - homo_recessive, file=outFile)
