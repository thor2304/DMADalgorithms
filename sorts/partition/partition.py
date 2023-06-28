# Partition method for quick sort
def partition(arr, low, high, one_indexed=False):
    if one_indexed:
        low = low - 1
        high = high - 1
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def main():
    A = [6, 2, 4, 5, 1, 7, 3]
    partition(A, 1, 7, one_indexed=True)

    print(A)


if __name__ == '__main__':
    main()
