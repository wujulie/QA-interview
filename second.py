n =0 #落地次數
high =0 #反彈高度
hight =100 #落地前n次高度
tour =0 #經過路程
for i in range(1,11):
    n = n+1
    tour = hight+high+tour #原始高度+反彈高度+上一次路程
    high = hight /2
    hight =high
    print("第{}次落地,總共{}公尺,第{}次反彈為{}公尺".format(n,tour,n,high))