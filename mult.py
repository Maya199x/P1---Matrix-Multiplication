import time
import os
import psutil
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3

#get the Process ID
pid = os.getpid()

#create a Process for the PSUTIL Library to monitor
process = psutil.Process(pid)

#save start time of the process
start_time = time.time()
print("Started at: " ,str(start_time))


cpu_start = process.cpu_percent()
mem_start = process.memory_info().rss

#create Matrix
A = np.random.rand(10**6, 10**3)
B = np.random.rand(10**3, 10**6)
C = np.random.rand(10**6, 1)


#calcualte multiplication of them
D = np.dot(B,C)
D = np.dot(A,D)

end_time = time.time()
print("Ended at: " ,str(end_time))
print("Difference is: ",str(end_time-start_time))
cpu_usage = []
mem_usage = []
time_points = []


while end_time >= start_time:
    print("time:", start_time)
    print(process.cpu_percent())
    cpu_usage.append(process.cpu_percent())
    mem_usage.append(process.memory_info().rss/1000000)
    time_points.append(start_time)
    start_time = start_time + 0.5

values, base = np.histogram(A)
cumulative = np.cumsum(values)





plt.plot(base[:-1], cumulative, c='blue', label='CDF')
plt.xlabel('Values')
plt.ylabel('Cumulative Probability')
plt.title('Empirical CDF of Matrix A')
plt.legend()
plt.show()

cpu_end = process.cpu_percent()
mem_end = process.memory_info().rss
cpu_delta = cpu_end - cpu_start
mem_delta = mem_end - mem_start


plt2.plot(time_points, cpu_usage, label='CPU Usage')
plt2.xlabel('Time (s)')
plt2.ylabel('Usage (%)')
plt2.legend()
plt2.show()


plt3.plot(time_points, mem_usage, label='Memory Usage')
plt3.xlabel('Time (s)')
plt3.ylabel('Usage (%)')
plt3.legend()
plt3.show()

# virtual ram
ramUsed = psutil.virtual_memory()
dictionUsed = dict(psutil.virtual_memory()._asdict())
percentage = psutil.virtual_memory().percent
print("percentage: ", percentage)
print("total used and availabel: " + str(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total) + " total: " + str(psutil.virtual_memory().total))
print("CPU usage: {}%".format(cpu_delta))
print("Memory usage: {} mb".format(mem_delta/1000000))
# https://stackoverflow.com/questions/15408371/cumulative-distribution-plots-python
