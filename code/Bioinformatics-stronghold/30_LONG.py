# rosalind_30_LONG
#
# Genome Assembly as Shortest Superstring
# https://rosalind.info/problems/long/
#
# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format 
# (which represent reads deriving from the same strand of a single linear chromosome).
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

# Genome Assembly as Shortest Superstring
# there exists a unique way to reconstruct the entire chromosome from these reads
# by gluing together pairs of reads that overlap by more than half their length.

# unique way. 절반 이상 겹치는 경우가 있으면, 반복적으로 합친다.
# unique way 이기 때문에, 합쳐진 서열이 제일 큰 부분이 겹치는 경우만 찾아도 됨
# 또는 모든 서열을 2개씩 비교하는 방법도 가능(greedy extension?)

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


def assembly(seqs: list):

    assembly_seq = seqs.pop()

    while seqs:
        flag = False

        for i in range(len(seqs)):  # seqs = ['ACCA', 'AACTC', 'AAAA']
            if flag:  # assembly
                break

            seq = seqs[i]  # seq = 'ACCA'
            for p in range(len(seq) // 2):
                q = len(seq) - p

                if assembly_seq.startswith(seq[p:]):
                    assembly_seq = seq[:p] + assembly_seq
                    flag = True
                    seqs.pop(i)
                    break
                elif assembly_seq.endswith(seq[:q]):
                    assembly_seq += seq[q:]
                    flag = True
                    seqs.pop(i)
                    break

    return assembly_seq


if __name__ == "__main__":

    file_path = './datasets/rosalind_long.txt'
    headers, seqs = parsing(file_path)

    with open("./answers/rosalind_long_outFile.txt", "w") as outFile:

        result_seq = assembly(seqs)
        print(f'{result_seq}', file=outFile)
