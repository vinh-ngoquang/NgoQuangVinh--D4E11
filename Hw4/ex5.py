congboi = 2
bar = int(input('How many B barterias are there: '))
time = int(input('How much time in minutes will we wait: '))
real_time = time / 2

total = bar * congboi ** (real_time)
print('After', time, 'minutes, we would have',int(total),'barterias')