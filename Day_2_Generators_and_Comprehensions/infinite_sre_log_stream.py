#Write a generator function follow_logs(file_obj) that uses a while True loop to check for new lines and yield them.

def follow_logs(file_obj):
    while True:
        line = file_obj.readline()
        if not line:
            break
        yield line

with open('log.txt', 'r') as file:
    for line in follow_logs(file):
        print(line)