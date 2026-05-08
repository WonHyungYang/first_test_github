def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    data = list(map(int, input("숫자를 공백으로 구분해 입력하세요: ").split()))
    print("정렬 전:", data)
    print("정렬 후:", bubble_sort(data))
