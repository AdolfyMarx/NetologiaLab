"""
Am actualy think about this, make todo
"""
import time


def time_now():
    return time.time()

print('thanks')
time_finish = time.time() + 3
while True:
    real_time = time_now()
    print(real_time)
    if time_finish <= real_time:
        break
print('finished')