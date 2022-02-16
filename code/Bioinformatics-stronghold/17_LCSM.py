# rosalind_17_LCSM
#
# Finding a Shared Motif
# https://rosalind.info/problems/lcsm/
#
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


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

# 1번 서열을 기준으로, 큰 부분부터 조각내서 다른 서열에 있는지 비교
if __name__ == "__main__":

    headers, seqs = parsing("./datasets/rosalind_lcsm.txt")
    lcs_flag = False
    lcs = ""

    for i in range(len(seqs[0]), 0, -1):  # 10, 9, 8, 7, ...
        if lcs_flag == True:
            break

        for j in range(len(seqs[0]) - i + 1):  # sequence slicing start point, 0 1 2 3 4 5 6
            count = 0
            for k in range(len(seqs)):  # find motif
                if seqs[0][j : j+i] in seqs[k]:
                    count += 1
                else:
                    break
            if count == len(seqs):  # if motif is in all sequence
                lcs = seqs[0][j : j+i]
                lcs_flag = True
                break

    with open("./answers/roslaind_lcsm_outFile.txt", "w") as outFile:
        print(lcs, file=outFile)
