# Danh sách các đồ vật với trọng lượng và giá trị
items = [
    {"item": 1, "weight": 2, "value": 20},
    {"item": 2, "weight": 5, "value": 30},
    {"item": 3, "weight": 10, "value": 50},
    {"item": 4, "weight": 5, "value": 10},
]

# Trọng lượng tối đa của túi
max_weight = 16

# Hàm sinh tất cả các tập hợp con bằng đệ quy
def generate_subsets_recursive(items, index=0):
    if index == len(items):
        return [[]]  # Khi duyệt hết danh sách, trả về tập hợp con rỗng

    # Lấy tất cả các tập hợp con không chứa phần tử hiện tại
    subsets_without_current = generate_subsets_recursive(items, index + 1)

    # Thêm phần tử hiện tại vào tất cả các tập hợp con đã tạo
    subsets_with_current = [subset + [items[index]] for subset in subsets_without_current]

    # Kết hợp cả hai
    return subsets_without_current + subsets_with_current

# Hàm tính tổng trọng lượng và giá trị của một tập hợp
def calculate_weight_value(subset):
    total_weight = sum(item["weight"] for item in subset)
    total_value = sum(item["value"] for item in subset)
    return total_weight, total_value

# Tìm tập hợp tốt nhất
def knapsack(items, max_weight):
    subsets = generate_subsets_recursive(items)  # Sinh tất cả các tập hợp con bằng đệ quy
    print(subsets)
    best_value = 0
    best_combination = []

    for subset in subsets:
        total_weight, total_value = calculate_weight_value(subset)
        if total_weight <= max_weight and total_value > best_value:
            best_value = total_value
            best_combination = subset

    return best_combination, best_value

# Gọi hàm và in kết quả
best_combination, best_value = knapsack(items, max_weight)

print("Các đồ vật được chọn:")
for item in best_combination:
    print(f"- Item {item['item']}: Weight = {item['weight']}, Value = {item['value']}")

print(f"Tổng trọng lượng: {sum(item['weight'] for item in best_combination)}")
print(f"Tổng giá trị: {best_value}")
