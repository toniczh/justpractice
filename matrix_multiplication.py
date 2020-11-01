import time
start=time.time()
# This preferred way to initialize an big list with 0
m_fill = [[0]*10000]*10000
stop=time.time()
print(stop-start)
start=time.time()
# 10000X10000 may take up to 7.8 seconds
m_fill = [[0 for i in range(10)] for j in range(10)]
stop=time.time()
print(stop-start)
# print(m_fill)
employees = []
employees.append({"name":"John Mckee","age":38,"Department":"Sales"})
employees.append({"name":"Lisa Crawford","age":29,"Department":"Marketing"})
employees.append({"name":"Sjuan Patel","age":33,"Department":"HR"})
print(employees)
patel = list(filter(lambda e: (e["name"]=="Sjuan Patel"),employees))
print(patel)
s=0.1+0.7
print(s)
import numpy as np
print(np.add(0.1,0.7))