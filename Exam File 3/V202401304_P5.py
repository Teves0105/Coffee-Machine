def nuclear_modifier(arr):
    new_list = []
    for number in arr:
        if number not in new_list and number!=0:
            new_list.append(number)

    new_list.extend([0]*(arr.count(0)))

    return new_list
arr = list(map(int, input().split()))
answer = nuclear_modifier(arr)
print(answer)