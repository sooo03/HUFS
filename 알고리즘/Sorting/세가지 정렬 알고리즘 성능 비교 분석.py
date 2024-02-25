# quick, merge, heap

import random, timeit


def quick_sort(A, first, last):
    global Qc, Qs #변수 선언
    if first >= last: return
    left, right = first+1, last
    pivot = A[first]
    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
            Qc += 1 #비교횟수+=1
        while right > first and A[right] >= pivot:
            right -= 1
            Qc += 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            Qs += 1
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]
    Qs += 1
    quick_sort(A, first, right-1)
    quick_sort(A, right+1, last)

#추가구현1
def insertion_sort(A, first, last):
    for i in range(1, n):
        j = i-1
        while j>=0 and A[j]>A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            j = j-1

def quick_sort_with_insertion_sort(A, first, last, k):    
    if last-first+1 <= k:
        insertion_sort(A, first, last)
    else:
        left, right = first + 1, last
        pivot = A[first]
        while left <= right:
            while left <= last and A[left] < pivot:
                left += 1
                Qc1 += 1
            while right > first and A[right] >= pivot:
                right -= 1
                Qc1 += 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                Qs += 1
                left += 1
                right -= 1
        A[first], A[right] = A[right], A[first]
        Qs1 += 1
        if k < 10 or k > 40:
            quick_sort_with_insertion_sort(A, first, right-1, k)
            quick_sort_with_insertion_sort(A, right+1, last, k)
        else:
            insertion_sort(A, first, right-1)
            insertion_sort(A, right+1, last)

#추가구현2
def new_quick_sort(A, first, last, k):
    if first >= last:
        return
    else:
        left, right = first+1, last
        p = A[first]
        while left <= right:
            while left <= last and A[left] < p:
                left += 1
            while right > first and A[right] >= p:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        A[first], A[right] = A[right], A[first]
        new_quick_sort(A, first, right-1, k)
        new_quick_sort(A, right+1, last, k)
        
def complete_sort_with_insertion_sort(A):
    insertion_sort(A, 0, len(A)-1)

def sort_with_quick_and_insertion_sort(A, k):
    quickSort(A, 0, len(A) - 1, k)
    complete_sort_with_insertion_sort(A)

def merge_sort(A, first, last):
    global Mc, Ms
    if first >= last: return
    middle = (first+last)//2
    merge_sort(A, first, middle)
    merge_sort(A, middle+1, last)
    B = []
    i = first
    j = middle+1
    while i <= middle and j <= last:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
            Mc += 1
        else:
            B.append(A[j])
            j += 1
            Mc += 1
    for i in range(i, middle+1):
        B.append(A[i])
        Ms += 1
    for j in range(j, last+1):
        B.append(A[j])
        Ms += 1
    for k in range(first, last+1):
        A[k] = B[k-first]
				
def new_merge(A, start, mid1, mid2, end):
    left_arr = A[start-1:mid1]
    mid_arr = A[mid1:mid2+1]
    right_arr = A[mid2+1:end]
    left_arr.append(float('inf'))
    mid_arr.append(float('inf'))
    right_arr.append(float('inf'))
    
    ind_left = 0
    ind_mid = 0
    ind_right = 0
    for i in range(start-1, end):
        minimum = min([left_arr[ind_left], mid_arr[ind_mid], right_arr[ind_right]])
        if minimum == left_arr[ind_left]:
            arr[i] = left_arr[ind_left]
            ind_left += 1
        elif minimum == mid_arr[ind_mid]:
            arr[i] = mid_arr[ind_mid]
            ind_mid += 1
        else:
            arr[i] = right_arr[ind_right]
            ind_right += 1

def three_way_merge_sort(A, first, last):
    if len(A[first-1:last])<2:
        return A
    else:
        mid1 = first + ((last-first)//3)
        mid2 = first + 2*((last-first)//3)
        three_way_merge_sort(A, first, mid1)
        three_way_merge_sort(A, mid1+1, mid2+1)
        three_way_merge_sort(A, mid2+2, end)
        new_merge(A, first, mid1, mid2, last)
        return A

def heapify_down(A, k, n):
    global Hc, Hs
    while 2*k+1 < n:
        L, R = 2*k+1, 2*k+2
        if L<n and A[L]>A[k]:
            m = L
            Hc += 1
        else:
            m = k
            Hc += 1
        if R<n and A[R] > A[m]:
            m = R
            Hc += 1
        if m != k:
            A[k], A[m] = A[m], A[k]
            k = m
            Hs += 1
        else:
            break

def make_heap(A):
    n = len(A)
    for k in range(n-1,-1, -1):
        heapify_down(A, k, n)

def heap_sort(A):
    n = len(A)
    make_heap(A)
    for k in range(len(A)-1, 0, -1):
        A[0], A[k] = A[k], A[0]
        n = n-1
        heapify_down(A, 0, n)

#추가구현4
def tim_sort(A):
    A.sort()


def check_sorted(A):
    for i in range(n-1):
        if A[i] > A[i+1]:
            return False
    return True


# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = [] # quick sort
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:] # merge
C = A[:] # heap
D = A[:] # 추가구현4

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Tim sort:")
print("time =", timeit.timeit("tim_sort(D)", globals=globals(), number=1))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D)) #추가구현4
