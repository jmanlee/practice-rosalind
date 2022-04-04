# rosalind_5_GC
#
# Computing GC Content
# https://rosalind.info/problems/gc/
#
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

from collections import Counter


class GC:
    def __init__(self, ID):
        self.ID = ID
        self.DNA = ""
        self.GC = None

  
if __name__ == "__main__":

    fasta_oj = []

    with open("./datasets/rosalind_gc.txt", "r") as inFile:
        for line in inFile.readlines():
            if line.startswith(">"):  # new string
                fasta_oj.append(GC(line[1:].strip()))
            else:  # sequence
                fasta_oj[-1].DNA += line.strip()  # remove \n

        for gc in fasta_oj:
            c = Counter(gc.DNA)
            gc.GC = (c["G"] + c["C"]) / sum(c.values())

        fasta_oj.sort(key=lambda x: x.GC)

    with open("./answers/rosalind_GC_outFile.txt", "w") as outFile:
        print(fasta_oj[-1].ID, fasta_oj[-1].GC * 100, sep="\n", file=outFile)
