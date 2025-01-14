def strf_scheduling(processes):
    """
    Hàm thực hiện giải thuật lập lịch SRT (Shortest Remaining Time).
    :param processes: Danh sách các tiến trình với thông tin (process_id, arrival_time, burst_time)
    :return: Bảng thông tin về các tiến trình sau khi lập lịch.
    """
    n = len(processes)
    remaining_time = [p[2] for p in processes]  # Thời gian thực thi còn lại của mỗi tiến trình
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    current_time = 0
    completed_count = 0
    prev = -1  # Tiến trình trước đó được chạy

    while completed_count < n:
        # Chọn tiến trình có thời gian thực thi còn lại nhỏ nhất trong số các tiến trình đã đến
        idx = -1
        min_remaining_time = float('inf')

        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0 and remaining_time[i] < min_remaining_time:
                min_remaining_time = remaining_time[i]
                idx = i

        if idx == -1:  # Không có tiến trình sẵn sàng
            current_time += 1
            continue

        # Giảm thời gian thực thi còn lại của tiến trình đang được chọn
        remaining_time[idx] -= 1
        current_time += 1

        # Nếu tiến trình hoàn thành, cập nhật thông tin
        if remaining_time[idx] == 0:
            completed_count += 1
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - processes[idx][1]
            waiting_time[idx] = turnaround_time[idx] - processes[idx][2]

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

# Thực thi giải thuật SRT
schedule = strf_scheduling(processes)

# In kết quả
print("STRF Scheduling:")
print("Input")
print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<12}")
for entry in schedule:
    print(f"{entry['Process ID']:<12}{entry['Arrival Time']:<15}{entry['Burst Time']:<12}")
print(" ")
print("Output")
print(f"{'Completion Time':<18}{'Turnaround Time':<18}{'Waiting Time':<12}")
for entry in schedule:    
    print(f"{entry['Completion Time']:<18}{entry['Turnaround Time']:<18}{entry['Waiting Time']:<12}")