def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = list(map(int, input("숫자를 공백으로 구분해 입력하세요: ").split()))
    print("정렬 전:", data)
    print("정렬 후:", insertion_sort(data))
