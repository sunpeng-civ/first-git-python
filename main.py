# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time

time01 = time.time()

a = ""

for i in range(100000):
    a += "sxt"

time02 = time.time()

print ("运算时间：" + str(time02-time01))

time03 = time.time()

li = []
for i in range(100000):
    li.append("sxt")

a = "".join(li)

time04 = time.time()

print ("运算时间：" + str(time04-time03))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
