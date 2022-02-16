# rosalind_21_MPRT
#
# Finding a Protein Moti
# https://rosalind.info/problems/mprt/
#
# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

"""
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: 
[XY] means "either X or Y" and {X} means "any amino acid except X." 
For example, the N-glycosylation motif is written as N{P}[ST]{P}.
"""

# 1) sample parsing
# 2) access tp https://www.uniprot.org/uniprot/~.fasta, AA parsing
# 3) N-glycosylation motif /N{P}[ST]{P}/
# 4) using regular expression

"""
1 >sp|B5ZC00|SYG_UREU1 Glycine--tRNA ligase OS=Ureaplasma urealyticum serovar 10 (strain ATCC 33699 / Western) OX=565575 GN=glyQS PE=3 SV=1
MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQ
KDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSS
...
"""

import re
import requests


def get_uniprot_sequence(accession: str):

    text = requests.get(f"http://www.uniprot.org/uniprot/{accession}.fasta").text  # not text()

    return "".join(line.strip() for line in text.splitlines()[1:])  # get().text is string. 


if __name__ == "__main__":

    with open("./datasets/rosalind_mprt.txt") as inFile:
        
        access_list = [line.strip() for line in inFile.readlines()]

    with open("./answers/rosalind_mprt_outFile.txt", "w") as outFile:

        # N-glycosylation motif /N{P}[ST]{P}/
        N_gly_dict = {}
        
        for accession in access_list:
            prot_seqeunce = get_uniprot_sequence(accession)
            # find N-gly motif
            N_gly_dict[accession] = [m.start() + 1 for m in re.finditer(r"(?=[N][^P][ST][^P])", prot_seqeunce)]  

        for accession, idx in N_gly_dict.items():
            if len(idx) > 0:
                print(accession, file=outFile)
                print(" ".join(map(str, idx)), file=outFile)
