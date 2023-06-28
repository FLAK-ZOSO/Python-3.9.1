def quickSort(num: list[int], min_: list[int], max_: list[int], i: int) -> None:
    if (len(num) in {0, 1}):
        return 0;
    p: int = num[0]
    if (p >= num[i]):
        max_[i] = num[i]
        i += 1
    else:
        min_[i] = num[i]
        i += 1
    return 1;


if __name__ == '__main__':
    num = [1, 5, 12, 8]
    min_: list[int] = [0 for _ in range(len(num))]
    max_: list[int] = [0 for _ in range(len(num))]
    i: int = 0
    quickSort(num, min_, max_, i)
    print(num)