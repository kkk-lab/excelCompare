#coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    line1=line1.split()
    line1=[int(x) for x in line1]
    # values1 = map(int, line1.split())
    # print(line1)
    line = sys.stdin.readline().strip()
    # values = map(int, line.split())
    line=line.split()
    line=[int(x) for x in line]
    if line1[0]==1:print(line1[0]);exit(0)
    copy=[x for x in line]
    for i in range(line1[0]):
        for j in range(i+1,line1[0]):
            if abs(line[i]-line[j])==line1[1]:
                # print(line[j],line[i])
                line[i]=123456789
                line[j]=123456789
                break
    # print(line)
    z=0
    for i in line:
        if i==123456789:
            z+=1
    y=len(line)-z/2
    if y==0:
        print(1)
    else:
        print(int(y))
