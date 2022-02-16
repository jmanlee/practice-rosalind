# rosalind_20_SPLC
#
# RNA Splicing
# https://rosalind.info/problems/splc/
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

"""
1. splicing site overlap?
2. T -> U
3. Translate to Amino Acids
4. stop codon check
"""

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


def parsing(file_path):

    with open(file_path) as inFile:

        headers, seqs = [], []
        for line in inFile.readlines():
            if line.startswith(">"):
                headers.append(line[1:].strip())
                seqs.append("")
            else:  # seqeunce
                seqs[-1] += line.strip()

    return headers, seqs


def RNA2AA(RNA: str):

    start = RNA.find("AUG")  # find start codon
    AA = []  # better memory usage than string concatenation

    for i in range(start, len(RNA), 3):
        codon = RNA[i : i+3]
        if CODON_TABLE[codon] == "Stop":
            break
        else:
            AA.append(CODON_TABLE[codon])

    return "".join(AA)


if __name__ == "__main__":

    headers, seqs = parsing("./datasets/rosalind_splc.txt")
    DNA, introns = seqs[0], seqs[1:]

    # splicing
    for seq in introns:
        DNA = DNA.replace(seq, "")

    # DNA to RNA
    RNA: str = DNA.replace("T", "U")

    with open("./answers/rosalind_splc_outFile.txt", "w") as outFile:

        AA = RNA2AA(RNA)
        print(AA, file=outFile)
