# rosalind_13_IEV
#
# Calculating Expected Offspring
# https://rosalind.info/problems/iev/
#
# Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. 
# In order, the six given integers represent the number of couples having the following genotypes:
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

if __name__ == "__main__":

    with open("./datasets/rosalind_iev.txt") as inFile:
        couple_list = map(int, inFile.readline().split())  # 1 0 0 1 0 1 // 

    with open("./answers/rosalind_iev_outFile.txt", "w") as outFile:
        # 1
        E = [2, 2, 2, 1.5, 1, 0]
        print(sum(e * c for e, c in zip(E, couple_list)), file=outFile)
