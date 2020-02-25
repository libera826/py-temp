from subprocess import *

def getCpuCount():
    r = check_output('sensors', shell=True).split()
    # for i in range(7, len(r), 9):
    #     print(i, r[i])
    return (len(r)-7)//9

def getTemp(id=-1):
    r = check_output('sensors', shell=True).split()
    if id == -2:    #CPU Package temperature
        return float(r[7][1:5])
    elif id == -1:
        temp = []
        for i in range(16, len(r), 9):
            temp.append(float(r[i][1:5]))
        return temp
    elif id < getCpuCount():
        return float(r[16+9*id][1:5])
    #exception