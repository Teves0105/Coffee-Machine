# Hàm tính tổng chi phí của một đường đi
def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # Quay về thành phố xuất phát
    return cost


# Hàm sinh tất cả các hoán vị (không dùng yield)
def generate_permutations(cities, start=0):
    permutations = []  # Danh sách để lưu các hoán vị
    if start == len(cities) - 1:
        permutations.append(cities[:])  # Lưu lại hoán vị hiện tại
    else:
        for i in range(start, len(cities)):
            cities[start], cities[i] = cities[i], cities[start]  # Hoán đổi
            permutations += generate_permutations(cities, start + 1)
            cities[start], cities[i] = cities[i], cities[start]  # Hoàn tác hoán đổi
    return permutations



# Hàm giải bài toán TSP không dùng thư viện và yield
def tsp_bruteforce(graph):
    n = len(graph)  # Số thành phố
    cities = list(range(n))  # Danh sách các thành phố: [0, 1, 2, ..., n-1]

    # Sinh tất cả các hoán vị
    all_permutations = generate_permutations(cities)

    # Tìm đường đi với chi phí nhỏ nhất
    min_cost = float('inf')
    best_path = None
    for perm in all_permutations:
        cost = calculate_cost(graph, perm)
        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return min_cost, best_path


# Ma trận khoảng cách (theo ví dụ từ hình ảnh)
graph = [
    [0, 2, 8, 5],  # Khoảng cách từ a (0) đến các thành phố khác
    [2, 0, 7, 3],  # Khoảng cách từ b (1) đến các thành phố khác
    [8, 7, 0, 4],  # Khoảng cách từ c (2) đến các thành phố khác
    [5, 3, 4, 0]  # Khoảng cách từ d (3) đến các thành phố khác
]

# Gọi hàm giải bài toán
min_cost, best_path = tsp_bruteforce(graph)

# In kết quả
print("Chi phí nhỏ nhất:", min_cost)
print("Hành trình tốt nhất:", " -> ".join(chr(97 + city) for city in best_path), "->", chr(97 + best_path[0]))
