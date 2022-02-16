# rosalind_12_PERM
#
# Enumerating Gene Orders
# https://rosalind.info/problems/perm/
#
# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

def permutation(nums: list):

    result = []

    if len(nums) == 1:
        return [nums]  # 이걸 리스트로 처리 안하면 concatenation error... [[1]]. 

    # for loop. permutation([1, 2, 3, 4]) => [2] + permutatioin([1, 3, 4]) 
    for i in range(len(nums)):
        result.extend([ [nums[i]] + perm for perm in permutation(nums[:i] + nums[i + 1:]) ]) # list comprehesion.
    
    return result


def permutation_num(n: int):

    return [i + 1 for i in range(n)]


if __name__ == "__main__":

    with open("./datasets/rosalind_perm.txt") as inFile:

        input_len = eval(inFile.readline())
        num_list = permutation_num(input_len)

    with open("./answers/rosalind_perm_outFile.txt", "w") as outFile:

        per_list = permutation(num_list)

        print(len(per_list), file=outFile)
        for p in per_list:  # p = [1, 2, 3]
            print(" ".join(map(str, p)), file=outFile) 


    # other's solution
    # permutation function...
    from itertools import permutations

    print(list(permutations(range(1, 4))))
