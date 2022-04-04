# rosalind_6_HAMM
#
# Counting Point Mutations
# https://rosalind.info/problems/hamm/
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

if __name__ == '__main__':
    
    with open('./datasets/rosalind_hamm.txt', 'r') as inFile:
        s, t = inFile.readlines() 

    with open('./answers/roslaind_hamm_outFile.txt', 'w') as outFile:
        #1
        print( sum( 1 for a, b in zip(s,t) if a != b) )

        #2. iterable onject에서 False, True의 sum이 계산 가능함.
        print( sum(a != b for a, b in zip(s,t)), file = outFile)


