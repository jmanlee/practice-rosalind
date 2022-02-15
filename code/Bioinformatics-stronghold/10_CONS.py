# rosalind_10_CONS
#
# Consensus and Profile
# https://rosalind.info/problems/cons/
#
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# DNA sequence의 각 index의 ATCG ratio 구하기

NUC2IDX = {"A": 0, "C": 1, "G": 2, "T": 3}
IDX2NUC = {0: "A", 1: "C", 2: "G", 3: "T"}


def make_profile(seqs):

    profile = [[0] * len(seqs[0]) for _ in range(4)]    #dictionary도 가능할 듯
    """
    profile = [
    A: [ 0, 0, 0, 0, 0, 0, 0]
    C: [ 0, 0, 0, 0, 0, 0, 0]
    T: [ 0, 0, 0, 0, 0, 0, 0]
    G: [ 0, 0, 0, 0, 0, 0, 0]
    ]
    """
    for seq in seqs:
        for i, nuc in enumerate(seq):
            profile[NUC2IDX[nuc]][i] += 1

    return profile


def make_consensus(profile):

    # profile ACGT의 각 자리의 숫자를 max로 비교,
    # 단, max로 비교하면서 어떤 nuc인지 index(0,1,2,3)를 확인해서 idx2nuc로 변환.
    # index를 비교하기 위해서, 각 ACTG 수를 [ ]로 만든 뒤, enumerate하여 lambda로 x[1]의 값을 비교하고 index인 x[0]을 리턴
    # 리턴된 index를 다시 idx2nuc로 ACTG 치환 및 연결.

    compare_profile = lambda x: max(enumerate(x), key=lambda k: k[1])[0]  # x = [45, 24, 56, 12], k = (0,45) / (1,24) ...
    prof_column = [[profile[i][j] for i in range(4)] for j in range(len(profile[0]))]    # [[45, 25, 56, 12], [0, 21, 1, 2], ...]

    return "".join(map(lambda col: IDX2NUC[compare_profile(col)], prof_column))


if __name__ == "__main__":

    with open("./datasets/rosalind_cons.txt") as inFile:

        seqs = []
        seq = ""
        inFile.readline()  # first line

        for line in inFile.readlines():
            if line.startswith(">"):  # string
                seqs.append(seq)
                seq = ""  # initialization
            else:
                seq += line.strip()

        seqs.append(seq)  # last line

    with open("./answers/rosalind_cons_outFile.txt", "w") as outFile:

        profile = make_profile(seqs)
        consensus = make_consensus(profile)

        print(consensus, file=outFile)
        for i in range(4):
            count = " ".join(map(str, profile[i])) # *map(str, profile[i]) // print(*profile[i])
            print(f"{IDX2NUC[i]}: {count}", file=outFile)

