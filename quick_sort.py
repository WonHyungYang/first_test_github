def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    data = list(map(int, input("숫자를 공백으로 구분해 입력하세요: ").split()))
    print("정렬 전:", data)
    print("정렬 후:", quick_sort(data))
