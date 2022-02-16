

# rosalind_16_FIBD

if __name__ == "__main__":

    with open("./datasets/rosalind_fibd.txt") as inFile:
        n, m = map(int, inFile.readline().split())  # n = nth month, can live for m momths. if n = 6 m = 3

        newborn = [1]
        adult = [0] * (m - 1)  # [0, 0] mth adult rabbit die...

        for i in range(n - 1):
            newborn.append(sum(adult))
            adult = [newborn[-2]] + adult[:-1]

    with open("./answers/roslaind_fibd_outFile.txt", "w") as outFile:
        print(newborn[-1] + sum(adult), file=outFile)


##DH's solution
def fibd(n, m):

    mat = [[0] * m for _ in range(n)]
    mat[0][0] = 1

    # newborn 부터
    for month in range(1, n):
        mat[month][0] = sum(mat[month - 1][1:])
        # adult
        for j in range(m - 1):
            mat[month][j + 1] = mat[month - 1][j]

    return sum(mat[-1])
