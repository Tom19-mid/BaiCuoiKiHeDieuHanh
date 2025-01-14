def fcfs_scheduling(processes):
    """
    Hàm thực hiện giải thuật lập lịch FCFS.
    :param processes: Danh sách các tiến trình với thông tin (process_id, arrival_time, burst_time)
    :return: Bảng thông tin về các tiến trình sau khi lập lịch.
    """
    # Sắp xếp các tiến trình theo thời gian đến
    processes.sort(key=lambda x: x[1])

    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # Tính toán thời gian hoàn thành, thời gian chờ, thời gian quay vòng
    current_time = 0
    for i in range(n):
        process_id, arrival_time, burst_time = processes[i]

        # Nếu CPU nhàn rỗi, đợi đến khi tiến trình đến
        if current_time < arrival_time:
            current_time = arrival_time

        # Thời gian hoàn thành của tiến trình
        completion_time[i] = current_time + burst_time

        # Cập nhật thời gian quay vòng và thời gian chờ
        turnaround_time[i] = completion_time[i] - arrival_time
        waiting_time[i] = turnaround_time[i] - burst_time

        # Cập nhật thời gian hiện tại
        current_time = completion_time[i]

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
    (2, 1, 3),
    (3, 2, 8),
    (4, 3, 6),
]

# Thực thi giải thuật FCFS
schedule = fcfs_scheduling(processes)

# In kết quả
print("FCFS Scheduling:")
print("Input")
print(f"{'Process ID':<12}{'Arrival Time':<15}{'Burst Time':<12}")
for entry in schedule:
    print(f"{entry['Process ID']:<12}{entry['Arrival Time']:<15}{entry['Burst Time']:<12}")

print(" ")
print("Output")
print(f"{'Completion Time':<18}{'Turnaround Time':<18}{'Waiting Time':<12}")
for entry in schedule:
    print(f"{entry['Completion Time']:<18}{entry['Turnaround Time']:<18}{entry['Waiting Time']:<12}")



