import random
from random import randint

TRIAL_COUNT = 5

def check_integer(num):
    if isinstance(num, int):
        return True
    else:
        return False

print('Enter the minimum and maximum values.\n')

# 最小値入力
while True:
    min = input('minimum ?\n')
    if check_integer(int(min)):
        break

# 最大値入力
while True: 
    max = input('maximum ?\n')
    if check_integer(int(max)) & int(min) < int(max):
        break

# 正解値生成
ans = randint(int(min), int(max))


# TRIAL_COUNT回試行するか、正解するまで繰り返す
for i in range(TRIAL_COUNT):
    input_num = input('Will you please, guess the number?')
    if ans == int(input_num):
        print('Correct!')
        break
    else: 
        print('Wrong!')



    