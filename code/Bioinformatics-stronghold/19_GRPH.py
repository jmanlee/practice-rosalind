# rosalind_19_GRPH
#
# Overlap Graphs
# https://rosalind.info/problems/grph/
#
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

from collections import defaultdict

def parsing(file_path):
    
    with open(file_path) as inFile:
        
        head, seq = [], []    
        for line in inFile.readlines():
            if line.startswith('>'):
                head.append(line[1:].strip())
                seq.append('')
            else: #seqeunce
                seq[-1] += line.strip()
                
    return head, seq

  
def overlap_graph(head: list, seq: list):
    
    k = 3
    suffix = defaultdict(list)
    prefix = defaultdict(list)
    
    for i in range(len(seq)):
        suffix[seq[i][-k:]].append(head[i])     #suffix{'aaa': [1, 2, 3], 'bbb': [5,6,7]}
        prefix[seq[i][:k]].append(head[i])
        
    result = []
                
    for dna in suffix:  #AAA, ACA, ..
        for s in suffix[dna]: # 1, 2, 3
            for p in prefix[dna]: #defaultdict
                if s != p:
                    result.append((s, p))
    
    return result

    
if __name__ == '__main__':
    
    head, seq = parsing('./datasets/rosalind_grph.txt')
    directed_graph = overlap_graph(head, seq)

    with open('./answers/rosalind_grph_outFile.txt', 'w') as outFile:
        
        for s, p in directed_graph:
            print(f'{s} {p}', file = outFile)
