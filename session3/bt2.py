quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
danso = [150330, 247100, 333300, 266800, 420900, 318000]

# max = danso.index(max(danso))             #1
# print(max)
# min = danso.index(min(danso))
# print(min)

# print(quan[max])
# print(quan[min])       #2

tongmd = 0
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
for i in range(len(danso)):
    md = float(danso[i]) / float(dientich[i])                    #4
    tongmd = tongmd + md
mdtb = tongmd / len(quan)
print(mdtb)

