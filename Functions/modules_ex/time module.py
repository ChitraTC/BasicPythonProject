import time
print(time.ctime())

import datetime
print(datetime.datetime.now())

print(time.time())
print(dir(datetime))
print(dir(time))

for i in range(5):
    time.sleep(1)
    print(i)