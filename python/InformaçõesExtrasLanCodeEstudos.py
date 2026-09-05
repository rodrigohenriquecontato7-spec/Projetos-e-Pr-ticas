from time import *
Time = int(input('Your Time: '))

while Time >=0:
    print(f'Time: {Time}')
    sleep(1)
    Time -=1
print("Time's Over!")