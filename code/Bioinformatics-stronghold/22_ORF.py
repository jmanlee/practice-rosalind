# rosalind_22_ORF
#
# Open Reading Frames
# https://rosalind.info/problems/orf/
#
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# 0 RNA transcription. forward? reverse?
# 1 find out M position 
# 2 translate until stop codon is found
# 3 if there is a stop codon, add protein sequence. If not, pass

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


import re


def ORF2Prot(DNA: str):

    protein_set = set()

    f_RNA = DNA.replace("T", "U")
    r_RNA = f_RNA.translate(str.maketrans("AUCG", "UAGC"))[::-1]

    f_RNA_start = [m.start() for m in re.finditer("AUG", f_RNA)]  # 전방탐색 쓸 필요 x 어차피 overlapping x
    r_RNA_start = [m.start() for m in re.finditer("AUG", r_RNA)]

    for RNA, RNA_start in [(f_RNA, f_RNA_start), (r_RNA, r_RNA_start)]:
        for start in RNA_start:
            AA = []
            for i in range(start, len(RNA)-2, 3):  # consider index error
                codon = RNA[i : i+3]
                if CODON_TABLE[codon] == "Stop":
                    protein_set.add("".join(AA))
                    break
                else:
                    AA.append(CODON_TABLE[codon])

    return protein_set


if __name__ == "__main__":

    with open("./datasets/rosalind_orf.txt") as inFile:
        DNA = "".join(line.strip() for line in inFile.readlines()[1:])

    with open("./answers/rosalind_orf_outFile.txt", "w") as outFile:
        protein_candidate = ORF2Prot(DNA)
        for protein in protein_candidate:
            print(protein, file=outFile)


