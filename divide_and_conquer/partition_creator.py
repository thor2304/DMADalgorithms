def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


if __name__ == '__main__':
    A = [21, 17, 28, 14, 9, 18, 6, 1, 26, 15, 30, 7, 13, 19, 2]
    print(partition(A, 3, 12)) # HUSK AT INDEKSER STARTER FRA 0, MEN AT OPGAVEN MÅSKE STARTER FRA 1
    print(A)