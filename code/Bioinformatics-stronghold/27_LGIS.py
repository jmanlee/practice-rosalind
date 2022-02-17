# rosalind_27_LGIS
#
# Longest Increasing Subsequence
# https://rosalind.info/problems/lgis/
#
# Given: A positive integer n≤10000 followed by a permutation π of length n.
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

# Dynamic programming?
# 1. 모든 증가 하는 부분 수열의 경우의 수를 구해서 max(list, key = len?)
# 2. n개의 개수를 갖는 sub_seq을 하나씩만 유지한다. 이 때, 가장 마지막값을 가장 작은 값이 되도록 업데이트한다.

# 1 brute force.. over time..
def LGIS_1(perm: list):  # Longest Iecreasing Subsequence

    result = []

    for num in perm:
        result.append([num])
        for l in result:
            if l[-1] < num:
                result.append(l + [num])

    return result, len(max(result, key=len))


def LGIS_2(perm: list):  # Longest Increasing Subsequence 

    result = []  # Ex) [[1], [1,2], [8,9,10], [8,9,10,11], ...] ,

    for num in perm:
        cache = []

        if not result:  # empty
            result = [[num]]
            continue

        for i in range(len(result)):
            if i == 0:  # first seq
                cache.append(min([result[i], [num]], key=lambda x: x[-1]))
            else:  # i >= 1
                if result[i - 1][-1] < num:  # update_possible
                    cache.append(min([result[i], result[i - 1] + [num]], key=lambda x: x[-1])                    )
                else:  # unpdate_impossible
                    cache.append(result[i])

        if result[-1][-1] < num:  # last seq append
            cache.append(result[-1] + [num])

        result = cache

    return result

def LGDS_2(perm: list):  # Longest Decreasing Subsequence 

    result = [] 

    for num in perm:
        cache = []

        if not result:  # empty
            result = [[num]]
            continue

        for i in range(len(result)):
            if i == 0:  # first seq
                cache.append(max([result[i], [num]], key=lambda x: x[-1]))
            else:  # i >= 1
                if result[i - 1][-1] > num:  # update_possible
                    cache.append(max([result[i], result[i - 1] + [num]], key=lambda x: x[-1])                    )
                else:  # unpdate_impossible
                    cache.append(result[i])

        if result[-1][-1] > num:  # last seq append
            cache.append(result[-1] + [num])

        result = cache

    return result


if __name__ == "__main__":

    with open("./datasets/rosalind_lgis.txt") as inFile:
        n = map(int, inFile.readline())
        perm = list(map(int, inFile.readline().split()))

    with open("./answers/rosalind_lgis_outFile.txt", "w") as outFile:

        lgis_seqs = LGIS_2(perm)
        lgds_seqs = LGDS_2(perm)

        print(' '.join(map(str, lgis_seqs[-1])), file=outFile)        
        print(' '.join(map(str, lgds_seqs[-1])), file=outFile)

        
#others solution
def solution(): #???? how...?
    
    inc = [(0,[])]*(n+1)
    l = []
    for i in l:
        x,y = max(inc[:i])
        inc[i] = (x+1,y+[i])

    print(" ".join(map(str,max(inc)[1])))


