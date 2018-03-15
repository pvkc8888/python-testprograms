#!/bin/python3


def surfaceArea(A, H, W):
    total_area = 2 * (H * W)
    for i in [0, H - 1]:
        for j in range(W):
            total_area += A[i][j]

    for i in [0, W - 1]:
        for j in range(H):
            total_area += A[j][i]

    for i in range(H):
        maxx = A[i][0]
        for j in range(1, W):
            if A[i][j] != maxx:
                total_area += abs(maxx - A[i][j])
                maxx = A[i][j]
    for i in range(W):
        maxx = A[0][i]
        for j in range(1, H):
            if A[j][i] != maxx:
                total_area += abs(maxx - A[j][i])
                maxx = A[j][i]

    return total_area


if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A, H, W)
    print(result)
