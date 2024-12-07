def compare_lists(list1, list2):
    try:
        assert list1 !=[] and list2 != [], "One or both lists are empty"
        q1 = [number for number in list1 if number not in list2]
        q2 = [number for number in list2 if number not in list1]
        q3 = [number for number in list1 if number in list2]
        q4 = q1 + q2 + q3
        q4.sort()
        return q1, q2, q3, q4
    except AssertionError as e:
        print(e)
    finally:
        pass
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(compare_lists(list1, list2))
