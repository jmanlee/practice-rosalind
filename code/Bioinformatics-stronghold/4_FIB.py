# rosalind_4_FIB
#
# Rabbits and Recurrence Relations
# https://rosalind.info/problems/fib/
#
# Given: Positive integers n≤40 and k≤5.
# The total number of rabbit pairs that will be present after n months, 
# if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# dynamic programming
if __name__ == '__main__':
    
    with open('./datasets/rosalind_fib.txt') as inFile:
        n, k = map(int, inFile.readline().split())

        newborn = [1]
        adult = [0]

        for i in range(n-1):
            newborn.append(adult[-1]*k)
            adult.append(adult[-1] + newborn[-2])
        
    with open('./answers/roslaind_fib_outFile.txt', 'w') as outFile:
        print( newborn[-1] + adult[-1], file = outFile )
