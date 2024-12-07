
def square_number(arr):
    try:
        assert arr != [], "Error"
        for i in range(len(arr)):
            arr[i] = arr[i]**2
        arr.sort()
        new_sorted_arr = [arr[i] for i in range(len(arr)) if i == 0 or arr[i]!=arr[i-1]]
        return new_sorted_arr
    except AssertionError as e:
        print(e)
arr = list(map(int, input().split()))

print(square_number(arr))