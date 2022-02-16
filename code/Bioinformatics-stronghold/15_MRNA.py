# rosalind_15_MRNA
#
# Inferring mRNA from Protein
# https://rosalind.info/problems/mrna/
#
# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
# (Don't neglect the importance of the stop codon in protein translation.)

from collections import defaultdict

RNA_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """.split()

# Please consider number of stop codon

if __name__ == "__main__":

    RNA_dict = dict(zip(RNA_table[::2], RNA_table[1::2]))
    AA_dict = defaultdict(int)

    for AA in RNA_dict.values():
        AA_dict[AA] += 1

    with open("./datasets/rosalind_mrna.txt") as inFile:
        protein = inFile.readline().strip()  # DNA string

    with open("./answers/rosalind_mrna_outFile.txt", "w") as outFile:
        # stop codon = 3
        result = 3
        for AA in protein:
            result *= AA_dict[AA]

        print(f"{result%1000000}", file=outFile)
