import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.virtual_memory())
print(psutil.swap_memory())
print(psutil.disk_partitions())

print('--------------------------')
print(psutil.net_if_addrs())
print('--------------------------')

print(psutil.net_if_stats())
print('--------------------------')
# print(psutil.net_connections())

# for i in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


print(psutil.pids())
p=psutil.Process(508)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(psutil.Process(p.ppid).name())

