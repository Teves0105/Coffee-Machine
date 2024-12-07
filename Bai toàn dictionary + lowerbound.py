import bisect


n = int(input())
arr = list(map(int, input().split()))
dict_count = {}

for i in range(len(arr)):
    if arr[i] not in dict_count:
        dict_count[arr[i]] = 1
    else:
        dict_count[arr[i]] += 1
    # dict_count[num] = dict_count.get(num, 0) + 1
t = int(input())
for i in range(t):
    two_value = input().split()
    first = int(two_value[0])
    second = int(two_value[1])

    if first == 1:
        if second in dict_count:
            dict_count[second] += 1
        else:
            dict_count[second] = 1
    elif first == 2:
        if second in dict_count:
            dict_count[second] -= 1
            if dict_count[second] == 0:
                del dict_count[second]

    elif first == 3:
            inter_list = sorted(dict_count.keys())
            index = bisect.bisect_left(inter_list, second)
            if index < len(inter_list):
                print(inter_list[index])
            else:
                print("-1")
    else:
        inter_list = sorted(dict_count.keys())
        index = bisect.bisect_right(inter_list, second) - 1
        if index >= 0:
            print(inter_list[index])
        else:
            print("-1")