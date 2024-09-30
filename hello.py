import random
i = 0; cnt = 0
while ( i < 10):
    rdnum = random.randint(0,100)
    print(rdnum, end = ' ')
    if (rdnum >= 0) and (rdnum <= 100):
        cnt += 1
    i += 1
print(f'The total is {cnt:10d}')