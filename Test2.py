import numpy as np

arr = np.array([1.1, 2.2, 3.3])
print(arr.dtype)
# Output: float64

int_arr = arr.astype(np.int32)
print(int_arr)
# Output: [1 2 3]

print(int_arr.dtype)
# Output: int32


