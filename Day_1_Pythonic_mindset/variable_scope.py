def process_logs(logs, new_entry):
    logs.append(new_entry)
    logs = ["CRITICAL FAILURE"] # Re-assignment
    return logs

my_logs = ["Info: System Start"]
processed = process_logs(my_logs, "Warning: Low Memory")

print(f"Original Logs: {my_logs}")
print(f"Returned Logs: {processed}")