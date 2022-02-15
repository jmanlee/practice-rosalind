# rosalind_9_SUBS
#
# Finding a Motif in DNA
# https://rosalind.info/problems/subs/
#
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

import re

if __name__ == "__main__":

    with open("./datasets/rosalind_subs.txt") as inFile:
        s = inFile.readline().strip()  # seq
        t = inFile.readline().strip()  # motif

        print(f"seq: {s}")
        print(f"motif: {t}")

        # 1
        result = []
        for i in range(len(s) - (len(t) - 1)):
            if s[i:].find(t) == 0:
                result.append(i + 1)

    with open("./answers/rosalind_subs_outFile.txt", "w") as outFile:
        # 2
        for i in range(len(s) - (len(t) - 1)):
            if s[i : i + len(t)] == t:
                print(f"{i+1}", end=" ", file=outFile)

        # 3 
        for i in range(len(s) - (len(t) - 1)):
            if s[i:].startswith(t):
                print("{0}".format(i + 1), end=" ")
        
        # 4 refer other's solution
        i = s.find(t)
        while i != -1:
            print(i + 1, end=" ")
            i = s.find(t, i + 1)  # start from index i+1
        
        # 5 using regular expression // 그냥 t, s 만 쓰면 결과값이 다름. overlapping이 안됨.
        print([m.start() + 1 for m in re.finditer(t, s)])
        
        # lookahead assertions // ?= // " " 안의 문자열 %s 를 %t로 처리
        print([m.start() + 1 for m in re.finditer("(?=%s)" % t, s)])
        
        # f string, lookahead assertions -> index overlapping // finditer은 generator임
        print([m.start() + 1 for m in re.finditer(f"(?={t})", s)])
