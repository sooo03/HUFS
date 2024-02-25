inf = int(1e9)

def max_sum(A, left, right):
   if left >= right: return A[left]
   
   m = (left + right) // 2
   L = max_sum(A, left, m)
   R = max_sum(A, m + 1, right)
   
   tmp, left_max = 0, -inf
   
   for i in range(m, left - 1, -1):
      tmp += A[i]
      left_max = max(left_max, tmp)
      
   tmp, right_max = 0, -inf
   
   for i in range(m + 1, right + 1):
      tmp += A[i]
      right_max = max(right_max, tmp)
      
   M = left_max + right_max
   
   return max(L, M, R)
    

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)