# rosalind_23_TRAN
#
# Transitions and Transversions
# https://rosalind.info/problems/tran/
#
# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).

# transition: purine to purine, pyrimidine to pyrimidine
# transversion: purine <-> pyrimidine

# 1 DNA parsing
# 2 transition, transversion

purines = ["A", "G"]
pyrimidines = ["C", "T"]


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


def is_transition(s1, s2):

    if (s1 in purines and s2 in purines) or (s1 in pyrimidines and s2 in pyrimidines):
        return True
    else:  # transversion
        return False


def get_transition_transversion_ratio(seq1, seq2):

    transition = 0
    transversion = 0

    for s1, s2 in zip(seq1, seq2):
        if s1 != s2:  # sequence change
            if is_transition(s1, s2):
                transition += 1
            else:
                transversion += 1

    return transition / transversion


if __name__ == "__main__":

    headers, seqs = parsing("./datasets/rosalind_tran.txt")  # two sequences of equal length

    with open("./answers/rosalind_tran_outFile.txt", "w") as outFile:

        t_t_ratio = get_transition_transversion_ratio(seqs[0], seqs[1])
        print(t_t_ratio, file=outFile)


""" 
    other's solution

    transition_dict = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

    transition_count = [1 if transition_dict[s1] == s2 else 0 for s1, s2 in zip(seq1, seq2) if s1 != s2]

    print(transition_count.count(1) / transition_count.count(0))
    
"""

