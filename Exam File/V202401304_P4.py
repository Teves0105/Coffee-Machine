def process_matrix(matrix):
    try:
        total = 0
        assert matrix != [] or all(element > 0 for row in matrix for element in row), "Found a non-positive element"
        matrix_list = [x for sub_matrix in matrix for x in sub_matrix]
        neg_matrix_list = [x for sub_matrix in matrix for x in sub_matrix if x>=0]
        cumulative_sum_list = []
        current_sum = 0
        for num in matrix_list:
            current_sum += num
            cumulative_sum_list.append(current_sum)

        return matrix_list, neg_matrix_list, cumulative_sum_list
    except AssertionError as e:
        print(e)
    finally:
        pass
matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [7, 8, 9]
]

print(process_matrix(matrix))

