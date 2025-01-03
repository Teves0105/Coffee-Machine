def job_scheduling(jobs):
    # Sắp xếp công việc theo lợi nhuận giảm dần
    jobs.sort(key=lambda x: x['Profit'], reverse=True)

    # Tìm deadline lớn nhất
    max_deadline = max(job['Deadline'] for job in jobs)

    # Khởi tạo danh sách thời gian trống
    time_slots = [None] * max_deadline  # Mỗi slot là 1 đơn vị thời gian
    total_profit = 0
    selected_jobs = []

    # Duyệt qua từng công việc
    for job in jobs:
        # Tìm thời gian trống gần nhất trước hoặc bằng deadline
        for t in range(job['Deadline'] - 1, -1, -1):
            if time_slots[t] is None:
                time_slots[t] = job['JobID']
                total_profit += job['Profit']
                selected_jobs.append(job['JobID'])
                break
    
    return selected_jobs, total_profit


# Test với dữ liệu
jobs = [
    {'JobID': 'a', 'Deadline': 4, 'Profit': 20},
    {'JobID': 'b', 'Deadline': 1, 'Profit': 10},
    {'JobID': 'c', 'Deadline': 1, 'Profit': 40},
    {'JobID': 'd', 'Deadline': 1, 'Profit': 30}
]

selected_jobs, total_profit = job_scheduling(jobs)
print("Công việc được chọn:", selected_jobs)
print("Tổng phần thưởng:", total_profit)
