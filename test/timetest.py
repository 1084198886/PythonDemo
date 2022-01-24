"""
time测试
"""
import calendar
import time

ticks = time.time()
print("当前时间戳:", ticks)
# print(dir(time.struct_time))
print()
print(time.localtime(ticks))
print("本地时间为 :", time.asctime(time.localtime(time.time())))  # Mon Jan 24 13:54:46 2022

fmttime = time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())
print(fmttime)  # 2022:01:24 13:57:43
print(time.strftime("%Y%m%d", time.localtime()))
print(time.strftime("%H%M%S", time.localtime()))
print(time.mktime(time.strptime(fmttime, "%Y:%m:%d %H:%M:%S")))

start = time.perf_counter_ns()
dur = time.perf_counter_ns() - start
print("时间差dur= %d ns" % (dur))

# 获取某月日历
cal = calendar.month(2022, 1)
print(cal)  # 输出2022年1月的日历：
"""
    January 2022
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
"""

print("timezone=", time.timezone)
print("tzname=", time.tzname)

print("firstweekday()=", calendar.firstweekday())  # 0即星期一
print("isleap=", calendar.isleap(2000))  # 是否是闰年
