def round_robin_scheduling(processes, quantum):
    """
    Hàm thực hiện giải thuật lập lịch Round Robin.
    :param processes: Danh sách các tiến trình với thông tin (process_id, arrival_time, burst_time)
    :param quantum: Thời lượng quantum (thời gian tối đa CPU cấp phát liên tục cho mỗi tiến trình)
    :return: Bảng thông tin về các tiến trình sau khi lập lịch.
    """
    n = len(processes)
    remaining_time = [p[2] for p in processes]  # Thời gian thực thi còn lại của mỗi tiến trình
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    current_time = 0
    queue = []  # Hàng đợi các tiến trình
    visited = [False] * n

    # Thêm các tiến trình đến ban đầu vào hàng đợi
    for i in range(n):
        if processes[i][1] == 0:
            queue.append(i)
            visited[i] = True

    while queue:
        idx = queue.pop(0)

        # Xử lý tiến trình hiện tại
        if remaining_time[idx] > quantum:
            current_time += quantum
            remaining_time[idx] -= quantum
        else:
            current_time += remaining_time[idx]
            remaining_time[idx] = 0
            completion_time[idx] = current_time

        # Kiểm tra các tiến trình mới đến
        for i in range(n):
            if not visited[i] and processes[i][1] <= current_time:
                queue.append(i)
                visited[i] = True

        # Nếu tiến trình hiện tại chưa hoàn thành, thêm lại vào cuối hàng đợi
        if remaining_time[idx] > 0:
            queue.append(idx)

    # Tính toán thời gian quay vòng và thời gian chờ
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

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
    (1, 0, 5),  # (Process ID, Arrival Time, Burst Time)
    (2, 1, 4),
    (3, 2, 2),
    (4, 3, 1),
]
quantum = 2

# Thực thi giải thuật Round Robin
schedule = round_robin_scheduling(processes, quantum)

# In kết quả
print("Round Robin Scheduling:")
print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<12}{'Completion Time':<18}{'Turnaround Time':<18}{'Waiting Time':<12}")
for entry in schedule:
    print(f"{entry['Process ID']:<12}{entry['Arrival Time']:<15}{entry['Burst Time']:<12}{entry['Completion Time']:<18}{entry['Turnaround Time']
                                                                                                                        <18}{entry['Waiting Time']:<12}")
