# first_test_github

## 정렬 알고리즘 (Sorting Algorithms)

### 1. 버블 정렬 (Bubble Sort)
인접한 두 원소를 비교하여 순서가 맞지 않으면 교환하는 방식으로, 가장 큰 값이 뒤로 밀려나는 구조입니다.

- **시간 복잡도:** O(n²)
- **공간 복잡도:** O(1)
- **특징:** 구현이 단순하지만 큰 데이터에는 비효율적

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

### 2. 선택 정렬 (Selection Sort)
전체에서 최솟값을 찾아 맨 앞 원소와 교환하는 방식을 반복합니다.

- **시간 복잡도:** O(n²)
- **공간 복잡도:** O(1)
- **특징:** 교환 횟수가 적어 메모리 쓰기 비용이 클 때 유리

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### 3. 삽입 정렬 (Insertion Sort)
정렬된 부분과 비교하며 현재 원소를 올바른 위치에 삽입합니다.

- **시간 복잡도:** O(n²) / 이미 정렬된 경우 O(n)
- **공간 복잡도:** O(1)
- **특징:** 거의 정렬된 데이터에 매우 효율적

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

### 4. 병합 정렬 (Merge Sort)
배열을 절반씩 나눠 재귀적으로 정렬한 뒤 합치는 분할 정복 방식입니다.

- **시간 복잡도:** O(n log n)
- **공간 복잡도:** O(n)
- **특징:** 안정 정렬, 큰 데이터에 적합

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

---

### 5. 퀵 정렬 (Quick Sort)
피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할하는 방식입니다.

- **시간 복잡도:** 평균 O(n log n) / 최악 O(n²)
- **공간 복잡도:** O(log n)
- **특징:** 평균적으로 가장 빠른 정렬 중 하나

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

---

### 복잡도 비교

| 알고리즘 | 평균 시간 | 최악 시간 | 공간 | 안정 정렬 |
|---------|----------|----------|------|---------|
| 버블 정렬 | O(n²) | O(n²) | O(1) | O |
| 선택 정렬 | O(n²) | O(n²) | O(1) | X |
| 삽입 정렬 | O(n²) | O(n²) | O(1) | O |
| 병합 정렬 | O(n log n) | O(n log n) | O(n) | O |
| 퀵 정렬   | O(n log n) | O(n²) | O(log n) | X |
