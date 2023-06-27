from bigO import BigO
lib = BigO()


def algo1(n):
    n: int = int(len(n))
    i: int = n
    while i > 1:
        j = n
        while j > i:
            j = j - 1
        i = i - 1


def algo2(n):
    n = len(n)
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            j = j*2
        i = i + 1


def algo3(n):
    n = len(n)
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            j = j+1
        i = i * 2


def algo4(n):
    n = len(n)
    i = 1
    j = 1
    while i <= n:
        while j <= i:
            j = j + 1
        i = i * 2


def algo5(n):
    n = len(n)
    i = n
    while i > 1:
        j = i
        while j < n:
            j = j + 1
        i = int(i / 2)


def algo6(n):
    n = len(n)
    s = 0
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                for k in range(1, n):
                    s = s + 1


def algo7(n):
    n = len(n)
    i = n
    j = n
    while i > 1:
        while j > i:
            j = j - 1
        i = i - 1


def algo8(n):
    n = len(n)
    i = 1
    while i < n:
        j = i
        while j > 1:
            j = j/2
        i = 2 * i


def algo9(n):
    n = len(n)
    i = n
    while i > 1:
        j = 1
        while j < i:
            j = 2*j
        i = i - 1


def algo10(n):
    n = len(n)
    for i in range(1, n):
        j = n - i
        while j < n:
            j = j + 1


def algo11(n):
    n = len(n)
    i = 1
    j = n
    while i < j:
        i = i + 1
        j = j - 1


def algo12(n):
    n = len(n)
    s = 0
    for i in range(1, n):
        s = i + s


def algo13(n):
    n = len(n)
    s = 1
    for i in range(1, n * n):
        for j in range(1, n):
            s = s+1


def algo14(n):
    n = len(n)
    i = n
    j = n
    while i <= j:
        j = j - 1
        i = 2 * i


def algo15(n):
    n = len(n)
    i = n
    s = 0
    while i >= 1:
        for j in range(i, 2 * i):
            s += 1
        i = i // 2


def algo16(n):
    n = len(n)
    s = 0
    for i in range(1, n):
        for j in range(i, n):
            s = s + 1


def algo17(n):
    n = len(n)
    for i in range(1, n):
        s = n
        while s > 1:
            s = s // 2


def algo18(n):
    n = len(n)
    s = 0
    for i in range(1, n):
        for j in range(i, n):
            for k in range(i, j):
                s = s + 1


def algo19(n):
    n = len(n)
    s = 0
    while n > 1:
        for i in range(1, n):
            s = s + 1
        n = n // 2


def main():
    print("Algo1")
    lib.test(algo1, "random")
    print("")

    print("Algo2")
    lib.test(algo2, "random")
    print("")

    print("Algo3")
    lib.test(algo3, "random")
    print("")

    print("Algo4")
    lib.test(algo4, "random")
    print("")

    print("Algo5")
    lib.test(algo5, "random")
    print("")

    print("Algo6")
    lib.test(algo6, "random")
    print("")

    print("Algo7")
    lib.test(algo7, "random")
    print("")

    print("Algo8")
    complexity = lib.test(algo8, "random")
    print(complexity)
    print("")

    print("Algo9")
    lib.test(algo9, "random")
    print("")

    print("Algo10")
    lib.test(algo10, "random")
    print("")

    print("Algo11")
    lib.test(algo11, "random")
    print("")

    print("Algo12")
    lib.test(algo12, "random")
    print("")

    print("Algo13")
    lib.test(algo13, "random")
    print("")

    print("Algo14")
    lib.test(algo14, "random")
    print("")

    print("Algo15")
    lib.test(algo15, "random")
    print("")

    print("Algo16")
    lib.test(algo16, "random")
    print("")

    print("Algo17")
    lib.test(algo17, "random")
    print("")

    print("Algo18")
    lib.test(algo18, "random")
    print("")

    print("Algo19")
    lib.test(algo19, "random")
    print("")

if __name__ == '__main__':
    main()