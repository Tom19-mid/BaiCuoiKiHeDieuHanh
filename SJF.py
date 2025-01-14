def sjf_scheduling(processes):
    """
    Hàm thực hiện giải thuật lập lịch SJF (Shortest Job First).
    :param processes: Danh sách các tiến trình với thông tin (process_id, arrival_time, burst_time)
    :return: Bảng thông tin về các tiến trình sau khi lập lịch.
    """
    n = len(processes)
    completed = [False] * n  # Theo dõi tiến trình nào đã hoàn thành
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # Sắp xếp tiến trình theo thời gian đến ban đầu
    processes.sort(key=lambda x: x[1])

    current_time = 0
    completed_count = 0

    while completed_count < n:
        # Chọn tiến trình có thời gian burst nhỏ nhất trong số các tiến trình đã đến
        idx = -1
        min_burst_time = float('inf')
        for i in range(n):
            if not completed[i] and processes[i][1] <= current_time and processes[i][2] < min_burst_time:
                min_burst_time = processes[i][2]
                idx = i

        if idx == -1:  # Nếu không có tiến trình nào sẵn sàng, tăng thời gian hiện tại
            current_time += 1
            continue

        # Xử lý tiến trình được chọn
        current_time += processes[idx][2]
        completion_time[idx] = current_time
        turnaround_time[idx] = completion_time[idx] - processes[idx][1]
        waiting_time[idx] = turnaround_time[idx] - processes[idx][2]
        completed[idx] = True
        completed_count += 1

    # Tạo bảng kết quả
    result = []
    for i in range(n):
        result.append({
            "Process ID": processes[i][0],
            "Arrival Time": processes[i][1],
            "Burst Time": processes[i][2],
            "Completion Time": completion_time[i],
            "Turnaround Time": turnaround_time[i],
            "Waiting Time": waiting_time[i],
        })

    return result

# Dữ liệu mẫu
processes = [
    (1, 0, 6),  # (Process ID, Arrival Time, Burst Time)
    (2, 1, 8),
    (3, 2, 7),
    (4, 3, 3),
]

# Thực thi giải thuật SJF
schedule = sjf_scheduling(processes)

# In kết quả
print("SJF Scheduling:")
print("Input")
print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<12}")
for entry in schedule:
    print(f"{entry['Process ID']:<12}{entry['Arrival Time']:<15}{entry['Burst Time']:<12}")
print(" ")
print("Outptut")
print(f"{'Completion Time':<18}{'Turnaround Time':<18}{'Waiting Time':<12}")
for entry in schedule:
    print(f"{entry['Completion Time']:<18}{entry['Turnaround Time']:<18}{entry['Waiting Time']:<12}")