def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    data = list(map(int, input("숫자를 공백으로 구분해 입력하세요: ").split()))
    print("정렬 전:", data)
    print("정렬 후:", selection_sort(data))
