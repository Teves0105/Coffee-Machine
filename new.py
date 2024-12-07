
n = int(input())
arr = list(map(str, input().split()))
dict_count = {}
for i in range(n):
    if arr[i] in dict_count:
        dict_count[arr[i]] += 1
    else:
        dict_count[arr[i]] = 1
sorted_dict_by_key = dict(sorted(dict_count.items()))

for i, item in enumerate(sorted_dict_by_key.items()):
    if i < 1:
        print(item[0], item[1])
    else:
        break
print()

i, item = next(reversed(sorted_dict_by_key.items()))
print(i, item)
print()

for i in sorted_dict_by_key.items():
    print(i[0], i[1])


for i in reversed(sorted_dict_by_key.items()):
    print(i[0], i[1])

