# rosalind_8_PROT
#
# Translating RNA into Protein
# https://rosalind.info/problems/prot/
#
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

RNA_codon_pair = """UUU F      CUU L      AUU I      GUU V
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

CODON_TABLE = dict(zip(RNA_codon_pair[0::2], RNA_codon_pair[1::2]))

if __name__ == "__main__":

    with open("./datasets/rosalind_prot.txt", "r") as inFile:
        AA = []
        rna = inFile.readline().strip()

        for i in range(0, len(rna), 3):
            codon = rna[i : i + 3]
            if CODON_TABLE[codon] == "Stop":
                break
            else:
                AA.append(CODON_TABLE[codon])

    with open("./answers/roslaind_prot_outFile.txt", "w") as outFile:
        print("".join(AA), file=outFile)
