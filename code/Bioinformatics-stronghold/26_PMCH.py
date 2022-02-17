# rosalind_26_PMCH
#
# Perfect Matchings and RNA Secondary Structures
# https://rosalind.info/problems/pmch/
#
# Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
# Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

# if C/G : 6, A/U : 8, possible number of perfect matching = 3! * 4!

from math import factorial as fac

if __name__ == "__main__":

    with open("./datasets/rosalind_pmch.txt") as inFile:

        RNA = "".join(line.strip() for line in inFile.readlines()[1:])

    with open("./answers/rosalind_pmch_outFile.txt", "w") as outFile:

        CG = RNA.count("C")
        AU = RNA.count("A")

        matching = fac(CG) * fac(AU)
        print(f"{matching}", file=outFile)
